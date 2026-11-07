import json, re
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer

docs=json.load(open("corpus.json",encoding="utf-8"))

def make_chunks():
    out=[]
    for doc_id,text in docs.items():
        spans=list(re.finditer(r"\S+",text))
        for i in range(0,len(spans),30):
            j=min(i+40,len(spans))
            if not spans: break
            out.append(dict(id=f"{doc_id}:{i//30}",doc=doc_id,
                            start=spans[i].start(),end=spans[j-1].end(),
                            text=text[spans[i].start():spans[j-1].end()]))
            if j==len(spans): break
    return out

chunks=make_chunks()
v=TfidfVectorizer()
C=v.fit_transform([c["text"] for c in chunks])
query=input("Question: ")
if not query.strip():
    print("Please enter a question.")
else:
    q=v.transform([query])
    if q.nnz==0:
        print("No matching records.")
    else:
        scores=(q@C.T).toarray()[0]
        for rank,i in enumerate(np.argsort(-scores)[:3],1):
            c=chunks[i]
            print(rank,c["id"],f"score={scores[i]:.3f}")
            print(c["text"])
            print("Source:",c["doc"],"characters",c["start"],c["end"])
