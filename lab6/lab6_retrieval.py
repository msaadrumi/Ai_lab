import time
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer

try:
    from sentence_transformers import SentenceTransformer
except ImportError:
    SentenceTransformer = None

QUERIES = [
    {"query": "What is required for illness extensions?", "doc": "late", "split": "dev",
     "evidence": "Illness extensions require medical evidence before the deadline."},
    {"query": "How do I reset a forgotten password?", "doc": "password", "split": "dev",
     "evidence": "Reset a forgotten password using the recovery link."},
    {"query": "Where do I upload assignments?", "doc": "assignment", "split": "dev",
     "evidence": "Upload assignments through the learning portal."},
    {"query": "Can contractors work remotely?", "doc": "contractor", "split": "dev",
     "evidence": "Contractors can work remotely only if the signed contract permits it."},
    {"query": "What do I do for blank printer pages?", "doc": "printer", "split": "test",
     "evidence": "For blank printer pages, check ink levels and run the cleaning utility."},
    {"query": "How can I recover my login access?", "doc": "password", "split": "test",
     "evidence": "Reset a forgotten password using the recovery link."},
    {"query": "How should I hand in my coursework?", "doc": "assignment", "split": "test",
     "evidence": "Upload assignments through the learning portal."},
    {"query": "What proof is needed when I was ill?", "doc": "late", "split": "test",
     "evidence": "Illness extensions require medical evidence before the deadline."},
    {"query": "What are tomorrow's flight prices?", "doc": None, "split": "test",
     "evidence": None},
    {"query": "Who won the football match?", "doc": None, "split": "test",
     "evidence": None},
]

def evaluate(scores, chunks, items):
    hits, reciprocal = [], []
    for row, q in zip(scores, items):
        if q["doc"] is None:
            continue
        top = np.argsort(-row, kind="stable")[:3]
        good = [
            rank for rank, i in enumerate(top, 1)
            if chunks[i]["doc"] == q["doc"]
            and q["evidence"] in chunks[i]["text"]
        ]
        hits.append(bool(good))
        reciprocal.append(1 / good[0] if good else 0)

    if not hits:
        return None, None
    return float(np.mean(hits)), float(np.mean(reciprocal))

def tfidf_run(chunks):
    texts = [c["text"] for c in chunks]
    queries = [q["query"] for q in QUERIES]
    vectorizer = TfidfVectorizer()
    C = vectorizer.fit_transform(texts)
    Q = vectorizer.transform(queries)
    return (Q @ C.T).toarray()

if __name__ == "__main__":
    print("Retrieval evaluation uses Hit@3 and MRR@3.")
    print("Run the supplied notebook for the full TF-IDF and MiniLM comparison.")
    print("The notebook's recorded development/test results are documented in Lab6_Report.docx.")
