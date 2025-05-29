import random


def bubble_sort(A):
    if len(A) == 0:
        return A

    for i in range(len(A) - 1):
        if A[i] > A[i + 1]:
            A[i], A[i + 1] = A[i + 1], A[i]

    return bubble_sort(A[:-1]) + [A[-1]]


w = [random.randrange(1000) for i in range(100)]
print(w)
ws = bubble_sort(w)
print(ws)
