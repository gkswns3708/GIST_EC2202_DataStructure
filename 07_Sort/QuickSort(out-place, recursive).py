import random


def quick_sort(A):
    if len(A) == 0:
        return A

    pivot = A[0]
    left = []
    right = []
    middle = []

    for a in A[1:]:
        if a < pivot:
            left.append(a)
        elif a == pivot:
            middle.append(a)
        else:
            right.append(a)

    return quick_sort(left) + middle + quick_sort(right)


n = 10000
w = [random.randrange(1000000) for i in range(n)]
print(w[:100])
w = quick_sort(w)  # out-place
print(w[:100])
