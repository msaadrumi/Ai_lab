from lab3_graph import GRAPH, START, GOAL


def dls(graph, start, goal, limit):
    path = []

    def visit(node, depth):
        path.append(node)

        if node == goal:
            return "FOUND", list(path)

        if depth == limit:
            path.pop()
            return "CUTOFF", None

        saw_cutoff = False

        for child in graph[node]:
            # Path-local cycle check
            if child in path:
                continue

            status, result = visit(child, depth + 1)

            if status == "FOUND":
                path.pop()
                return "FOUND", result

            if status == "CUTOFF":
                saw_cutoff = True

        path.pop()

        if saw_cutoff:
            return "CUTOFF", None

        return "FAILURE", None

    return visit(start, 0)


def run_dls():
    for limit in [1, 2, 3, 4]:
        status, path = dls(GRAPH, START, GOAL, limit)
        print(f"DLS limit {limit}: {status}")
        print("Path:", " -> ".join(path) if path else "None")


def iddfs(graph, start, goal, max_depth):
    attempts = []

    for limit in range(1, max_depth + 1):
        status, path = dls(graph, start, goal, limit)
        attempts.append((limit, status, path))

        if status == "FOUND":
            return status, path, attempts

    return "CUTOFF", None, attempts


if __name__ == "__main__":
    run_dls()

    print("\nIDDFS")
    for max_depth in [1, 2, 3, 4]:
        status, path, attempts = iddfs(
            GRAPH, START, GOAL, max_depth
        )

        limits = [limit for limit, _, _ in attempts]

        print(f"IDDFS maximum depth {max_depth}: {status}")
        print("Limits attempted:", limits)
        print("Path:", " -> ".join(path) if path else "None")
