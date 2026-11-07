from lab5_tree import LEAVES
from lab5_minimax import minimax
from lab5_alphabeta import alpha_beta

def run_case(name, values):
    mm_count = [0]
    ab_count = [0]
    ab_trace = []

    mm_value = minimax(values, mm_count)
    ab_value = alpha_beta(values, ab_count, ab_trace)

    print("\n" + name)
    print("Leaves:", values)
    print("Minimax value:", mm_value)
    print("Minimax leaves evaluated:", mm_count[0])
    print("Alpha-beta value:", ab_value)
    print("Alpha-beta leaves evaluated:", ab_count[0])
    print("Alpha-beta terminal values visited:", ab_trace)
    print("Pruned leaves:", mm_count[0] - ab_count[0])

    assert mm_value == ab_value

if __name__ == "__main__":
    run_case("Original left-to-right order", LEAVES)

    # Same values, but branches are reordered.
    reordered = [5, 3, 9, 2, 3, 5, 9, 2]
    run_case("Reordered branches", reordered)
