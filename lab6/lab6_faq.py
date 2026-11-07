from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np

FAQ = [
    {
        "question": "How do I reset my password?",
        "answer": "Use the recovery link on the login page.",
        "source": "it_help.txt",
    },
    {
        "question": "Where do I submit my assignment?",
        "answer": "Use the assignment upload page in the learning portal.",
        "source": "assessment.txt",
    },
    {
        "question": "Can illness justify a late submission?",
        "answer": "Request an extension with medical evidence before the deadline.",
        "source": "handbook.txt",
    },
    {
        "question": "How do I check my assignment receipt?",
        "answer": "Open the learning portal and check your submission history.",
        "source": "portal_guide.txt",
    },
    {
        "question": "Why does my printer print blank pages?",
        "answer": "Check ink levels and run the cleaning utility.",
        "source": "it_help.txt",
    },
]

texts = [x["question"] + " " + x["answer"] for x in FAQ]
vectorizer = TfidfVectorizer()
matrix = vectorizer.fit_transform(texts)

def reply(query):
    if not query.strip():
        return "Please enter a question."

    for item in FAQ:
        if query.strip().casefold() == item["question"].casefold():
            return item["answer"] + " [source: " + item["source"] + "]"

    q = vectorizer.transform([query])
    if q.nnz == 0:
        return "No matching FAQ. Please contact the help desk."

    scores = (q @ matrix.T).toarray()[0]
    order = np.argsort(-scores, kind="stable")[:3]

    lines = ["Possible matches; choose or rephrase your question:"]
    for i in order:
        if scores[i] > 0:
            lines.append(
                FAQ[i]["question"] + f" (similarity {scores[i]:.3f})"
            )

    if len(lines) == 1:
        return "No matching FAQ. Please contact the help desk."
    return "\n".join(lines)

if __name__ == "__main__":
    print(reply("How do I reset my password?"))
    print(reply("password recovery"))
    print(repr(reply("")))
    print(reply("volcano geology"))

    assert "it_help.txt" in reply("How do I reset my password?")
    assert reply("") == "Please enter a question."
    assert "No matching FAQ" in reply("volcano geology")
    assert "Possible matches" in reply("password recovery")
    print("FAQ behaviour checks passed")
