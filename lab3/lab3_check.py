from lab3_graph import GRAPH
from lab3_bfs_dfs import bfs, dfs
from lab3_depth_search import dls, iddfs
from lab3_ucs import WEIGHTS, ucs, path_cost, bfs_weighted_topology

bfs_path, bfs_order = bfs(GRAPH, "A", "G")
assert bfs_path == ["A", "B", "D", "G"]
assert bfs_order == ["A", "B", "C", "D", "E", "F", "G"]

dfs_path, dfs_order = dfs(GRAPH, "A", "G")
assert dfs_path == ["A", "B", "D", "G"]
assert dfs_order == ["A", "B", "D", "G"]

for limit in [1, 2]:
    status, path = dls(GRAPH, "A", "G", limit)
    assert status == "CUTOFF"
    assert path is None

status, path = dls(GRAPH, "A", "G", 3)
assert status == "FOUND"
assert path == ["A", "B", "D", "G"]

status, path = dls(GRAPH, "A", "G", 4)
assert status == "FOUND"
assert path == ["A", "B", "D", "G"]

status, path, attempts = iddfs(GRAPH, "A", "G", 1)
assert status == "CUTOFF"
assert [x[0] for x in attempts] == [1]

status, path, attempts = iddfs(GRAPH, "A", "G", 2)
assert status == "CUTOFF"
assert [x[0] for x in attempts] == [1, 2]

status, path, attempts = iddfs(GRAPH, "A", "G", 3)
assert status == "FOUND"
assert path == ["A", "B", "D", "G"]
assert [x[0] for x in attempts] == [1, 2, 3]

status, path, attempts = iddfs(GRAPH, "A", "G", 4)
assert status == "FOUND"
assert path == ["A", "B", "D", "G"]
assert [x[0] for x in attempts] == [1, 2, 3]

cost, path, processed = ucs(WEIGHTS, "A", "G")
assert path == ["A", "C", "G"]
assert cost == 6
assert path_cost(path, WEIGHTS) == 6

bfs_path = bfs_weighted_topology(WEIGHTS, "A", "G")
assert bfs_path == ["A", "B", "D", "G"]
assert path_cost(bfs_path, WEIGHTS) == 8

print("All Lab 3 checks passed.")
