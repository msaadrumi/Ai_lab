from heapq import heappush, heappop
from lab4_graph import GRAPH, HEURISTIC, START, GOAL

def astar(graph, heuristic):
    frontier = []
    g_score = {START: 0}
    parent = {START: None}
    heappush(frontier, (g_score[START] + heuristic[START], g_score[START], START))

    expanded = []
    trace = []

    while frontier:
        f, g, node = heappop(frontier)

        # Ignore an old heap entry if a better g value is already known.
        if g != g_score.get(node):
            trace.append(("STALE", node, g, f))
            continue

        expanded.append(node)
        trace.append(("EXPAND", node, g, heuristic[node], f))

        if node == GOAL:
            break

        for child, cost in graph[node]:
            new_g = g + cost
            if new_g < g_score.get(child, float("inf")):
                g_score[child] = new_g
                parent[child] = node
                new_f = new_g + heuristic[child]
                heappush(frontier, (new_f, new_g, child))

    if GOAL not in g_score:
        return None, float("inf"), expanded, trace

    path = []
    node = GOAL
    while node is not None:
        path.append(node)
        node = parent[node]
    path.reverse()

    return path, g_score[GOAL], expanded, trace


def ucs(graph):
    zero_h = {node: 0 for node in graph}
    return astar(graph, zero_h)


def run():
    print("A*")
    path, cost, expanded, trace = astar(GRAPH, HEURISTIC)
    print("Path:", " -> ".join(path))
    print("Cost:", cost)
    print("Expanded:", expanded)
    print("Expansion count:", len(expanded))
    print("Trace:", trace)

    print("\nUCS (zero heuristic)")
    path, cost, expanded, trace = ucs(GRAPH)
    print("Path:", " -> ".join(path))
    print("Cost:", cost)
    print("Expanded:", expanded)
    print("Expansion count:", len(expanded))
    print("Trace:", trace)


if __name__ == "__main__":
    run()
