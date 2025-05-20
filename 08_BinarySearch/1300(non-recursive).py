import sys
get_line: iter = lambda: map(int, sys.stdin.readline().rstrip().split())
get_input: int = lambda: int(sys.stdin.readline().strip())

def binary_search(N, K):
    def possible(N, mid, K):
        count = 0
        for i in range(1, N + 1):
            count += min(mid // i, N)
        return count >= K
    left = 0
    right = 10 ** 9
    while left <= right:
        mid = (left + right) // 2
        if possible(N, mid, K):
            result = mid
            right = mid - 1
        else:
            left = mid + 1
    return result


def solution():
    N = get_input()
    K = get_input()
    
    print(binary_search(N, K))

if __name__ == "__main__":
    solution()