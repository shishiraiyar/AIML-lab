def f(x):
    return -(x-2)**2 + 4

def hillClimbSearch(start=0, step = 0.1, max_iter=10000):
    maxima = start
    maxValue = f(maxima)
    for i in range(max_iter):
        left = maxima - step
        right = maxima + step

        if f(left) > maxValue and f(left) >= f(right):
            maxima = left
            maxValue = f(left)
            continue
        elif f(right) > maxValue:
            maxima = right
            maxValue = f(right)

    return maxima, maxValue

print(hillClimbSearch())
        