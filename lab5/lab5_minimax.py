from lab5_tree import LEAVES

def minimax(values, count):
    def solve(index, depth):
        if depth == 3:
            count[0] += 1
            return values[index]

        left = solve(index * 2, depth + 1)
        right = solve(index * 2 + 1, depth + 1)

        if depth % 2 == 0:   # MAX
            return max(left, right)
        else:                # MIN
            return min(left, right)

    return solve(0, 0)
