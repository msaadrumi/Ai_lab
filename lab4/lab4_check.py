from lab4_astar import astar, ucs
from lab4_graph import GRAPH, HEURISTIC

p1, c1, e1, _ = astar(GRAPH, HEURISTIC)
p2, c2, e2, _ = ucs(GRAPH)

bad_h = dict(HEURISTIC)
bad_h["C"] = 10
p3, c3, e3, _ = astar(GRAPH, bad_h)

assert p1 == ["S", "A", "C", "G"]
assert c1 == 6
assert p2 == ["S", "A", "C", "G"]
assert c2 == 6
assert p3 == ["S", "B", "G"]
assert c3 == 9

print("All Lab 4 checks passed.")
