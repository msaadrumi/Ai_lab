import re
import time

samples = [
    "AI, search!",
    "I can't log in.",
    "help@example.com",
    "CS4944 version 2.1",
    "",
    "میں یونیورسٹی جا رہا ہوں",
]

for text in samples:
    ws = text.split()
    words = re.findall(r"\b\w+\b", text, flags=re.UNICODE)
    print(repr(text))
    print("Whitespace:", ws, len(ws))
    print("Word-like:", words, len(words))

try:
    from sentence_transformers import SentenceTransformer
    start = time.perf_counter()
    model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2", device="cpu")
    print("Model load seconds:", round(time.perf_counter() - start, 2))
    print("Model token limit:", model.max_seq_length)
    for text in samples[:2]:
        tokens = model.tokenizer.tokenize(text)
        print(repr(text), "Model tokens:", tokens, len(tokens))
except Exception as e:
    print("Model tokenizer unavailable in this environment:", e)
