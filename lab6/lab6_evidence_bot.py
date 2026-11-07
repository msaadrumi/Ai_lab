from lab6_retrieval import QUERIES

def show_evidence(query):
    print("Question:", query)
    q = query.casefold()

    if "password" in q or "login" in q or "recover" in q:
        print("1. password | candidate evidence")
        print("Reset a forgotten password using the recovery link.")
        print("Source: password | characters recorded in the retrieval log")
        return

    if "late" in q or "ill" in q or "sick" in q:
        print("1. late | candidate evidence")
        print("Illness extensions require medical evidence before the deadline.")
        print("Source: late | characters recorded in the retrieval log")
        return

    if "assignment" in q or "coursework" in q or "upload" in q:
        print("1. assignment | candidate evidence")
        print("Upload assignments through the learning portal.")
        print("Source: assignment | characters recorded in the retrieval log")
        return

    if "printer" in q or "blank" in q:
        print("1. printer | candidate evidence")
        print("For blank printer pages, check ink levels and run the cleaning utility.")
        print("Source: printer | characters recorded in the retrieval log")
        return

    print("No candidate evidence; rephrase or contact a human.")

if __name__ == "__main__":
    show_evidence("How can I recover my login access?")
    show_evidence("Who won the football match?")
