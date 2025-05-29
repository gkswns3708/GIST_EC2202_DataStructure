import sys

N = int(sys.stdin.readline())

arr = [-1] * (N + 2)
arr[1] = 1
arr[0] = 0


def fib(i):
    if arr[i] != -1:
        return arr[i]
    else:
        arr[i] = fib(i - 2) + fib(i - 1)
        return arr[i]


print(fib(N))
