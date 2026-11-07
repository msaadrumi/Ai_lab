from lab4_astar import astar
from lab4_graph import GRAPH, HEURISTIC

def path_cost(path):
    total = 0
    for a, b in zip(path, path[1:]):
        for child, cost in GRAPH[a]:
            if child == b:
                total += cost
                break
    return total

def show_result(title, graph, heuristic):
    path, cost, expanded, trace = astar(graph, heuristic)
    print(title)
    print("Heuristic:", heuristic)
    print("Path:", " -> ".join(path))
    print("Reported cost:", cost)
    print("Independent path cost:", path_cost(path))
    print("Expanded:", expanded)
    print("Expansion count:", len(expanded))
    print("Trace:", trace)
    print()

if __name__ == "__main__":
    show_result("Original A*", GRAPH, HEURISTIC)

    changed = dict(HEURISTIC)
    changed["C"] = 10
    show_result("Overestimate experiment: h(C)=10", GRAPH, changed)

    print("Original h(C):", HEURISTIC["C"])
    print("Modified h(C):", changed["C"])
    print("True remaining cost from C to G: 3")
