# Lab 3 - BFS, DFS, DLS, IDDFS and UCS

## Folder structure

```text
lab3/
├── lab3_graph.py
├── lab3_bfs_dfs.py
├── lab3_depth_search.py
├── lab3_ucs.py
├── lab3_check.py
├── lab3_frontier_traces.txt
├── lab3_bfs_dfs_output.txt
├── lab3_depth_output.txt
├── lab3_ucs_output.txt
├── lab3_check_output.txt
├── README.md
└── Lab3_Report.docx
```

## Requirements

Python 3.10+ is recommended. The code uses only the Python standard library.

## Run BFS and DFS

```bash
cd lab3
python lab3_bfs_dfs.py
```

## Run DLS and IDDFS

```bash
python lab3_depth_search.py
```

## Run UCS

```bash
python lab3_ucs.py
```

## Run checks

```bash
python lab3_check.py
```

## Graph assumptions

The original A-G graph used here is:

```text
A -> B, C
B -> D, E
C -> F
D -> G
E -> none
F -> none
G -> none
```

The successor order is exactly the order shown above. Start is A and goal is G.
For DLS/IDDFS, A is depth 0 and the cycle check is path-local.

## Weighted extension

The weighted version keeps the original topology and adds one controlled corridor:
C -> G with weight 2.

Weights:
A-B=1
A-C=4
B-D=2
B-E=1
C-F=2
C-G=2
D-G=5

This makes the BFS route A-B-D-G have fewer hops but a higher cost (8) than the
UCS route A-C-G (6).

## Reproducibility

No credentials, private information, or virtual environments are included.
