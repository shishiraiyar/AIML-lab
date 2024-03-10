import random
def f(x):
    return -(x-2)**2 + 4

def hillClimbSearch(f, start=0, step = 0.1, max_iter=100):
    minima = start
    minValue = f(minima)
    for i in range(max_iter):
        left = minima - step
        right = minima + step

        if f(left) > minValue and f(left) >= f(right):
            minima = left
            minValue = f(left)
            continue
        elif f(right) > minValue:
            minima = right
            minValue = f(right)

    return minima, minValue


print(hillClimbSearch(f))
        