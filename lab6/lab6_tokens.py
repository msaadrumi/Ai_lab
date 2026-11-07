import re

samples = [
    "AI, search!",
    "I can't log in.",
    "help@example.com",
    "CS4944 version 2.1",
    "",
    "میں یونیورسٹی جا رہا ہوں",
]

for text in samples:
    whitespace = text.split()
    word_like = re.findall(r"\b\w+\b", text, flags=re.UNICODE)
    print("Original:", repr(text))
    print("Whitespace:", whitespace, "count =", len(whitespace))
    print("Word-like:", word_like, "count =", len(word_like))
    print()

try:
    from transformers import AutoTokenizer
    tokenizer = AutoTokenizer.from_pretrained(
        "sentence-transformers/all-MiniLM-L6-v2"
    )
    for text in samples[:2]:
        tokens = tokenizer.tokenize(text)
        print("Model tokens:", repr(text), tokens, "count =", len(tokens))
except Exception as e:
    print("Model tokenizer unavailable:", e)
