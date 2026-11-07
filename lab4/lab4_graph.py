# lab4 graph data
GRAPH = {
    "S": [("A", 1), ("B", 4)],
    "A": [("C", 2)],
    "B": [("G", 5)],
    "C": [("G", 3)],
    "G": []
}

HEURISTIC = {
    "S": 5,
    "A": 4,
    "B": 4,
    "C": 2,
    "G": 0
}

START = "S"
GOAL = "G"
