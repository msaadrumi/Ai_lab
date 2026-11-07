# Lab 5 - Minimax and Alpha-Beta Pruning

## Files
- `lab5_tree.py` - 8-leaf complete tree values.
- `lab5_minimax.py` - Minimax with a terminal-leaf counter.
- `lab5_alphabeta.py` - Alpha-beta pruning with a terminal-leaf counter.
- `lab5_minimax_alphabeta.py` - runs original and reordered cases.
- `lab5_check.py` - verification checks.
- `lab5_output.txt` - captured outputs.
- `lab5_manual_trace.txt` - hand trace.
- `Lab5_Report.docx` - report.

## Run
```bash
python lab5_minimax_alphabeta.py
python lab5_check.py
```

The tree uses the supplied complete 8-leaf example:
`[3, 5, 2, 9, 3, 5, 2, 9]`

The root is MAX, the next level is MIN, and the next level is MAX. Leaves are evaluated left-to-right.

## Branch reordering
The reordered case is:
`[5, 3, 9, 2, 3, 5, 9, 2]`

The multiset of leaf values is unchanged. The Minimax root value remains 5, while alpha-beta evaluates fewer leaves.

No credentials, private data, or virtual environments are included.
