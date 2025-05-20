import sys
get_line: iter = lambda: map(int, sys.stdin.readline().rstrip().split())
get_input: int = lambda: int(sys.stdin.readline().strip())

def binary_search(trees, M):
    def possible(trees, length, M):
        count = 0
        for tree in trees:
            count += max(tree-length, 0)
        return count >= M
    left = -1
    right = max(trees)
    result = -1
    while left <= right:
        mid = (left + right) // 2
        if possible(trees, mid, M):
            result = mid
            left = mid + 1
        else:
            right = mid - 1
    return result


def solution():
    N, M = get_line()
    trees = list(get_line())
    print(binary_search(trees, M))
    
if __name__ == "__main__":
    solution()