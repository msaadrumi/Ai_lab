from lab5_tree import LEAVES
from lab5_minimax import minimax
from lab5_alphabeta import alpha_beta

for values in [LEAVES, [5, 3, 9, 2, 3, 5, 9, 2]]:
    a = [0]
    b = [0]
    trace = []
    va = minimax(values, a)
    vb = alpha_beta(values, b, trace)
    assert va == vb == 5
    assert a[0] == 8

print("All Lab 5 checks passed.")
