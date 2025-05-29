import random


def insert_sort(A):
    if len(A) == 0:
        return A

    for i in range(1, len(A)):
        for j in range(0, i):
            if A[i] < A[j]:
                A[i], A[j] = A[j], A[i]

    return A


w = [random.randrange(1000) for i in range(100)]
print(w)
ws = insert_sort(w)
print(ws)
