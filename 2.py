INFINITY = 1000

def minimax(depth, index, maximizingPlayer, array, alpha, beta):
    if depth == 3:
        return array[index]

    if maximizingPlayer:
        best = -INFINITY
        # Recur for left and right children
        for i in [0, 1]:
            if (2*index + i) >=len(array):
                return array[index]
            val = minimax(depth + 1, index * 2 + i, False, array, alpha, beta)
            best = max(best, val)
            alpha = max(alpha, best)

            if beta <= alpha:
                break
        return best

    else:
        best = INFINITY

        for i in [0, 1]:
            if (2*index + i) >=len(array):
                return array[index]
            val = minimax(depth + 1, index * 2 + i, True, array, alpha, beta)
            best = min(best, val)
            beta = min(beta, best)

            if beta <= alpha:
                break
        return best



if __name__ == "__main__":
    values = [3, 5, 6, 9, 1, 2, 0, -1]
    print("The optimal value is :", minimax(0, 0, True, values, -INFINITY, INFINITY))