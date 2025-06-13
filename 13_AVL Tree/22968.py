# https://www.acmicpc.net/problem/22968
import sys

get_line: iter = lambda: map(int, sys.stdin.readline().rstrip().split())
get_input: int = lambda: int(sys.stdin.readline().strip())


def cal_node():
    ret = [0 for _ in range(50)]
    ret[1], ret[2] = 1, 2  # base case
    for i in range(3, 50):
        ret[i] = ret[i - 1] + ret[i - 2] + 1
    return ret


def f(n, ret):
    for i in range(len(ret) - 1, 0, -1):
        if ret[i] <= n:
            return i
    return -1


def solution():
    N = get_input()
    ret = cal_node()
    for _ in range(N):
        n = get_input()
        print(f(n, ret))


if __name__ == "__main__":
    solution()
