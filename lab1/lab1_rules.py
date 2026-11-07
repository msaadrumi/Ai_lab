# Lab 1 - Rule-based scholarship example
# The thresholds below are synthetic lab assumptions.

def check_scholarship(score, documents_complete, attendance, income):
    if score < 70:
        return False, "score is below 70"

    if not documents_complete:
        return False, "required documents are incomplete"

    # Additional transparent condition 1
    if attendance < 75:
        return False, "attendance is below the 75% requirement"

    # Additional transparent condition 2
    if income > 50000:
        return False, "income is above the Rs. 50,000 requirement"

    return True, "all synthetic scholarship conditions are satisfied"


# Exactly four core test cases
cases = [
    {
        "name": "Pass",
        "score": 80,
        "documents_complete": True,
        "attendance": 85,
        "income": 40000,
        "expected": True
    },
    {
        "name": "Attendance failure",
        "score": 80,
        "documents_complete": True,
        "attendance": 70,
        "income": 40000,
        "expected": False
    },
    {
        "name": "Income failure",
        "score": 80,
        "documents_complete": True,
        "attendance": 85,
        "income": 60000,
        "expected": False
    },
    {
        "name": "Threshold boundary",
        "score": 70,
        "documents_complete": True,
        "attendance": 75,
        "income": 50000,
        "expected": True
    }
]

for case in cases:
    actual, reason = check_scholarship(
        case["score"],
        case["documents_complete"],
        case["attendance"],
        case["income"]
    )

    print("Case:", case["name"])
    print("Input:", {
        "score": case["score"],
        "documents_complete": case["documents_complete"],
        "attendance": case["attendance"],
        "income": case["income"]
    })
    print("Expected result:", case["expected"])
    print("Actual result:", actual)
    print("Reason:", reason)
    print("-" * 45)
