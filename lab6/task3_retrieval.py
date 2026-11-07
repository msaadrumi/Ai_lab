import csv
import json
import time
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer

docs = json.load(open("corpus.json", encoding="utf-8"))
queries = json.load(open("queries.json", encoding="utf-8"))

try:
    from sentence_transformers import SentenceTransformer
except ImportError:
    SentenceTransformer = None

# Same chunking/retrieval procedure as the supplied notebook.
def word_spans(text):
    return [(m.start(), m.end()) for m in __import__("re").finditer(r"\S+", text)]

def windows(text, size=40, overlap=10, offset=0):
    if size <= 0 or not 0 <= overlap < size:
        raise ValueError("Require size > 0 and 0 <= overlap < size")
    spans = word_spans(text)
    result = []
    if not spans:
        return result
    for i in range(0, len(spans), size - overlap):
        j = min(i + size, len(spans))
        result.append((offset + spans[i][0], offset + spans[j - 1][1]))
        if j == len(spans):
            break
    return result

def sentence_chunks(text, size=40):
    cuts = [0] + [m.end() for m in __import__("re").finditer(r"[.!?]\s+", text)] + [len(text)]
    out, pending, count = [], None, 0
    for a, b in zip(cuts, cuts[1:]):
        segment = text[a:b]
        n = len(segment.split())
        if not n:
            continue
        if n > size:
            if pending is not None:
                out.append(pending)
            out.extend(windows(segment, size, 0, a))
            pending, count = None, 0
        elif pending is not None and count + n <= size:
            pending, count = (pending[0], b), count + n
        else:
            if pending is not None:
                out.append(pending)
            pending, count = (a, b), n
    if pending is not None:
        out.append(pending)
    return out

def make_chunks(strategy):
    result = []
    for doc_id, text in docs.items():
        spans = sentence_chunks(text) if strategy == "sentence" else windows(text, 40, int(strategy))
        for i, (a, b) in enumerate(spans):
            result.append(dict(id=f"{doc_id}:{i}", doc=doc_id, start=a, end=b, text=text[a:b]))
    return result

def evaluate(scores, chunks, items):
    hits, reciprocal = [], []
    for row, q in zip(scores, items):
        if q["doc"] is None:
            continue
        top = np.argsort(-row, kind="stable")[:3]
        good = [rank for rank, i in enumerate(top, 1)
                if chunks[i]["doc"] == q["doc"] and q["evidence"] in chunks[i]["text"]]
        hits.append(bool(good))
        reciprocal.append(1 / good[0] if good else 0)
    return float(np.mean(hits)), float(np.mean(reciprocal))

if SentenceTransformer is None:
    print("Embedding backend unavailable. Install sentence-transformers to reproduce embedding rows.")
else:
    model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2", device="cpu")
    logs = []
    for strategy in ["0", "10", "sentence"]:
        chunks = make_chunks(strategy)
        texts = [c["text"] for c in chunks]
        query_texts = [q["query"] for q in queries]
        lengths = [len(model.tokenizer(t, truncation=False)["input_ids"]) for t in texts + query_texts]
        print(strategy, "chunks:", len(chunks), "| max tokens:", max(lengths), "| limit:", model.max_seq_length)

        for method in ["tfidf", "embedding"]:
            t = time.perf_counter()
            if method == "tfidf":
                vectorizer = TfidfVectorizer()
                C = vectorizer.fit_transform(texts)
                Q = vectorizer.transform(query_texts)
            else:
                C = model.encode(texts, normalize_embeddings=True)
                Q = model.encode(query_texts, normalize_embeddings=True)
            encode_seconds = time.perf_counter() - t

            t = time.perf_counter()
            scores = (Q @ C.T).toarray() if method == "tfidf" else Q @ C.T
            search_seconds = time.perf_counter() - t

            for split in ["dev", "test"]:
                indices = [i for i, q in enumerate(queries) if q["split"] == split]
                result = evaluate(scores[indices], chunks, [queries[i] for i in indices])
                print(strategy, method, split, "Hit@3/MRR@3:",
                      tuple(round(x, 3) for x in result),
                      "| encode:", round(encode_seconds, 3),
                      "search:", round(search_seconds, 4))

            for row, q in zip(scores, queries):
                for rank, i in enumerate(np.argsort(-row, kind="stable")[:3], 1):
                    c = chunks[i]
                    logs.append(dict(strategy=strategy, method=method, query=q["query"],
                                     split=q["split"], rank=rank, score=round(float(row[i]), 3),
                                     chunk_id=c["id"], doc=c["doc"], start=c["start"], end=c["end"],
                                     text=c["text"], answerable=q["doc"] is not None))

    with open("retrieval_log.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(logs[0]))
        writer.writeheader()
        writer.writerows(logs)
    print("retrieval_log.csv rows:", len(logs))
