import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer

FAQ = [
    {"id": "faq:password", "question": "How do I reset my password?",
     "answer": "Use the recovery link on the login page.", "source": "it_help.txt"},
    {"id": "faq:submit", "question": "Where do I submit my assignment?",
     "answer": "Use the assignment upload page in the learning portal.", "source": "assessment.txt"},
    {"id": "faq:late", "question": "Can illness justify a late submission?",
     "answer": "Request an extension with medical evidence before the deadline.", "source": "handbook.txt"},
    {"id": "faq:receipt", "question": "How do I check my assignment receipt?",
     "answer": "Open the learning portal and check your submission history.", "source": "portal_guide.txt"},
    {"id": "faq:blank", "question": "Why does my printer print blank pages?",
     "answer": "Check ink levels and run the cleaning utility.", "source": "it_help.txt"},
]

class FAQBot:
    def __init__(self):
        texts = [x["question"] + " " + x["answer"] for x in FAQ]
        self.vectorizer = TfidfVectorizer()
        self.matrix = self.vectorizer.fit_transform(texts)

    def reply(self, query):
        if not query.strip():
            return "Please enter a question."
        for item in FAQ:
            if query.strip().casefold() == item["question"].casefold():
                return item["answer"] + " [source: " + item["source"] + "]"
        q = self.vectorizer.transform([query])
        if q.nnz == 0:
            return "No matching FAQ. Please contact the help desk."
        scores = (q @ self.matrix.T).toarray()[0]
        order = np.argsort(-scores, kind="stable")[:3]
        lines = ["Possible matches; choose or rephrase your question:"]
        for i in order:
            lines.append(FAQ[i]["question"] + f" (similarity {scores[i]:.3f})")
        return "\n".join(lines)

def build_faq_bot():
    return FAQBot()
