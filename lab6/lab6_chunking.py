import re

def word_spans(text):
    return [(m.start(), m.end()) for m in re.finditer(r"\S+", text)]

def windows(text, size=40, overlap=10, offset=0):
    if size <= 0 or not 0 <= overlap < size:
        raise ValueError("Require size > 0 and 0 <= overlap < size")

    spans = word_spans(text)
    result = []
    step = size - overlap

    for i in range(0, len(spans), step):
        j = min(i + size, len(spans))
        if i >= len(spans):
            break
        result.append((offset + spans[i][0], offset + spans[j - 1][1]))
        if j == len(spans):
            break
    return result

def sentence_chunks(text, size=40):
    if size <= 0:
        raise ValueError("size must be positive")

    cuts = [0] + [m.end() for m in re.finditer(r"[.!?]\s+", text)] + [len(text)]
    out = []
    pending = None
    count = 0

    for a, b in zip(cuts, cuts[1:]):
        segment = text[a:b]
        n = len(segment.split())
        if not n:
            continue

        if n > size:
            if pending is not None:
                out.append(pending)
                pending = None
                count = 0
            out.extend(windows(segment, size, 0, a))
        elif pending is not None and count + n <= size:
            pending = (pending[0], b)
            count += n
        else:
            if pending is not None:
                out.append(pending)
            pending = (a, b)
            count = n

    if pending is not None:
        out.append(pending)
    return out

def make_chunks(docs, strategy):
    result = []
    for doc_id, text in docs.items():
        spans = sentence_chunks(text) if strategy == "sentence" else windows(
            text, 40, int(strategy)
        )
        for i, (start, end) in enumerate(spans):
            result.append({
                "id": f"{doc_id}:{i}",
                "doc": doc_id,
                "start": start,
                "end": end,
                "text": text[start:end],
            })
    return result

if __name__ == "__main__":
    text = "Reset your password. Keep recovery codes private."
    print("Empty text:", windows(""))
    print("Short document:", windows("short text"))

    try:
        windows("a b", 2, 2)
    except ValueError:
        print("Invalid overlap: ValueError raised")

    long_text = " ".join(["word"] * 95) + "."
    print(
        "95-word sentence split into:",
        [len(long_text[a:b].split()) for a, b in sentence_chunks(long_text)]
    )
