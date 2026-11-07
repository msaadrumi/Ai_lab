from lab5_tree import LEAVES

def alpha_beta(values, count, trace):
    def solve(index, depth, alpha, beta):
        if depth == 3:
            count[0] += 1
            trace.append(values[index])
            return values[index]

        if depth % 2 == 0:   # MAX
            value = float("-inf")
            for child in (index * 2, index * 2 + 1):
                value = max(value, solve(child, depth + 1, alpha, beta))
                alpha = max(alpha, value)
                if alpha >= beta:
                    break
            return value

        value = float("inf")  # MIN
        for child in (index * 2, index * 2 + 1):
            value = min(value, solve(child, depth + 1, alpha, beta))
            beta = min(beta, value)
            if alpha >= beta:
                break
        return value

    return solve(0, 0, float("-inf"), float("inf"))
