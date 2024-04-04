INFINITY = 10000

def minimax(depth, nodeIndex, maximisingPlayer, values, alpha, beta):
    if depth == 3:
        return values[nodeIndex]
	
    if maximisingPlayer:
        best = -INFINITY
        for i in range(0, 2):
            score = minimax(depth+1, nodeIndex*2 + i, False, values, alpha, beta)
            best = max(best, score)
            alpha = max(alpha, best)

            if beta<=alpha:
                break
    else:
        best = INFINITY
        for i in range(0, 2):
            score = minimax(depth+1, nodeIndex*2+i, True, values, alpha, beta)
            best = min(best, score)
            beta = min(beta, best)

            if beta<=alpha:
                break
    return best
	
if __name__ == "__main__": 
    #values = [3, 5, 6, 9, 1, 2, 0, -1]
    values = [6, -5, 2, 3, 1, 2, 0, -1]
    print("The optimal value is :", minimax(0, 0, True, values, -INFINITY, INFINITY)) 
