# Lab 4 - A* Heuristic Audit and UCS Comparison

## Files
- `lab4_graph.py` - supplied weighted graph and heuristic.
- `lab4_astar.py` - A* and zero-heuristic UCS implementation.
- `lab4_astar_audit.py` - independent path-cost audit and overestimate experiment.
- `lab4_check.py` - reproducibility checks.
- `lab4_output.txt` - captured program output.
- `lab4_manual_trace.txt` - manual first-three-expansion trace.
- `Lab4_Report.docx` - report.

## Graph
S -> A (1)
S -> B (4)
A -> C (2)
B -> G (5)
C -> G (3)

Start = S
Goal = G

Heuristic:
h(S)=5, h(A)=4, h(B)=4, h(C)=2, h(G)=0

## Run
```bash
python lab4_astar_audit.py
python lab4_astar.py
python lab4_check.py
```

No credentials, private data, or virtual environment are included.

## Tie-breaking
Priority entries are ordered as `(f, g, node)`. Thus smaller f is selected first; if f ties, smaller g is preferred; if both tie, the node name gives a deterministic final tie-break.
