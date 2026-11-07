import json
from task2_chunks import make_chunks
docs=json.load(open("corpus.json",encoding="utf-8"))
chunks=make_chunks(docs,"10")
query="How can I recover my login access?"
for c in chunks:
    if c["doc"]=="password" and "Reset a forgotten password" in c["text"]:
        print("Question:",query)
        print("Candidate evidence:",c["text"])
        print("Source:",c["doc"],"characters",c["start"],c["end"])
        break
