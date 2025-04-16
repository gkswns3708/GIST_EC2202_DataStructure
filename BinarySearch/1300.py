import sys
sys.setrecursionlimit(10**9)
get_line: iter = lambda: map(int, sys.stdin.readline().rstrip().split())
get_input: int = lambda: int(sys.stdin.readline().strip())

def binary_search(N, left, right, K):
    def possible(N, mid, K):
        count = 0
        for i in range(1, N + 1):
            count += min(mid // i, N)
        return count >= K
    
    mid = (left + right) // 2
    if left <= right:
        if possible(N, mid, K):
            return min(mid, binary_search(N, left, mid - 1, K))
        else:
            return binary_search(N, mid + 1, right, K)
    else:
        return left


def solution():
    N = get_input()
    K = get_input()
    
    print(binary_search(N, 0, 10 ** 10, K))

if __name__ == "__main__":
    solution()