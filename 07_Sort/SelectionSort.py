import random


def find_min_index(A):
    min_idx = 0
    for i in range(1, len(A)):
        if A[i] < A[min_idx]:
            min_idx = i
    return min_idx


def selection_sort(A):
    if len(A) == 0:
        return A

    k = find_min_index(A)
    return [A[k]] + selection_sort(A[:k] + A[k + 1 :])


# w = [random.randrange(1000) for i in range(100) ]
# print(w)
# ws = selection_sort(w)
# print(ws)
