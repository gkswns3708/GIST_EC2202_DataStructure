import sys

sys.setrecursionlimit(10**3 * 5)

get_line: iter = lambda: map(int, sys.stdin.readline().rstrip().split())
get_input: int = lambda: int(sys.stdin.readline().strip())


def merge(a, b):
    i = 0
    j = 0
    res = []
    while i < len(a) and j < len(b):
        va = a[i]
        vb = b[j]
        if compare(va, vb) == -1 or compare(va, vb) == 0:
            res.append(va)
            i += 1
        else:
            res.append(vb)
            j += 1
    # now just copy remaining elements
    # (only one of these can be non-empty)
    res.extend(a[i:])
    res.extend(b[j:])
    return res


def merge_sort(a):
    if len(a) <= 1:
        return a
    mid = len(a) // 2
    left_half = merge_sort(a[:mid])
    right_half = merge_sort(a[mid:])
    return merge(left_half, right_half)


def compare(x, y):
    if x[0] > y[0]:
        return 1
    elif x[0] == y[0]:
        if x[2] > y[2]:
            return 1
        elif x[2] == y[2]:
            return 0
        else:
            return -1
    else:
        return -1


N = get_input()
input_arr = []
for i in range(N):
    a, b = sys.stdin.readline().rstrip().split()
    input_arr.append((int(a), b, i))

sorted_arr = merge_sort(input_arr)
for i in sorted_arr:
    print(i[0], i[1])
