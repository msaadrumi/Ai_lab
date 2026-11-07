import heapq

# Controlled weighted extension of the original A-G graph.
# Added corridor: C -> G with weight 2.
WEIGHTS = {
    "A": [("B", 1), ("C", 4)],
    "B": [("D", 2), ("E", 1)],
    "C": [("F", 2), ("G", 2)],
    "D": [("G", 5)],
    "E": [],
    "F": [],
    "G": []
}


def ucs(graph, start, goal):
    frontier = [(0, 0, start, [start])]
    best_cost = {start: 0}
    counter = 0
    processed = []

    while frontier:
        cost, _, node, path = heapq.heappop(frontier)

        if cost != best_cost.get(node):
            continue

        processed.append((node, cost))

        if node == goal:
            return cost, path, processed

        for child, weight in graph[node]:
            new_cost = cost + weight

            if new_cost < best_cost.get(child, float("inf")):
                best_cost[child] = new_cost
                counter += 1
                heapq.heappush(
                    frontier,
                    (new_cost, counter, child, path + [child])
                )

    return None, None, processed


def path_cost(path, graph):
    total = 0

    for a, b in zip(path, path[1:]):
        for child, weight in graph[a]:
            if child == b:
                total += weight
                break

    return total


def bfs_weighted_topology(graph, start, goal):
    from collections import deque

    queue = deque([(start, [start])])
    visited = set()

    while queue:
        node, path = queue.popleft()

        if node in visited:
            continue

        visited.add(node)

        if node == goal:
            return path

        for child, _ in graph[node]:
            if child not in visited:
                queue.append((child, path + [child]))

    return None


if __name__ == "__main__":
    ucs_cost, ucs_path, processed = ucs(WEIGHTS, "A", "G")
    bfs_path = bfs_weighted_topology(WEIGHTS, "A", "G")
    bfs_cost = path_cost(bfs_path, WEIGHTS)

    print("UCS processing order:")
    print(" -> ".join(f"{node}({cost})" for node, cost in processed))

    print("UCS path:", " -> ".join(ucs_path))
    print("UCS returned cost:", ucs_cost)
    print("UCS independently summed cost:", path_cost(ucs_path, WEIGHTS))

    print("BFS path on same weighted topology:", " -> ".join(bfs_path))
    print("BFS path cost:", bfs_cost)

    print("\nEdge weights:")
    for node, edges in WEIGHTS.items():
        for child, weight in edges:
            print(f"{node} -> {child} = {weight}")
