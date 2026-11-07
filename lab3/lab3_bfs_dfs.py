from collections import deque
from lab3_graph import GRAPH, START, GOAL


def bfs(graph, start, goal):
    queue = deque([(start, [start])])
    visited = set()
    order = []

    while queue:
        node, path = queue.popleft()

        if node in visited:
            continue

        visited.add(node)
        order.append(node)

        if node == goal:
            return path, order

        for child in graph[node]:
            if child not in visited:
                queue.append((child, path + [child]))

    return None, order


def dfs(graph, start, goal):
    stack = [(start, [start])]
    visited = set()
    order = []

    while stack:
        node, path = stack.pop()

        if node in visited:
            continue

        visited.add(node)
        order.append(node)

        if node == goal:
            return path, order

        # Reverse so the first successor is processed first.
        for child in reversed(graph[node]):
            if child not in visited:
                stack.append((child, path + [child]))

    return None, order


if __name__ == "__main__":
    bfs_path, bfs_order = bfs(GRAPH, START, GOAL)
    dfs_path, dfs_order = dfs(GRAPH, START, GOAL)

    print("BFS path:", " -> ".join(bfs_path))
    print("BFS visit order:", " -> ".join(bfs_order))

    print("DFS path:", " -> ".join(dfs_path))
    print("DFS visit order:", " -> ".join(dfs_order))
