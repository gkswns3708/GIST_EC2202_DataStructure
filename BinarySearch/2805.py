import sys
get_line: iter = lambda: map(int, sys.stdin.readline().rstrip().split())
get_input: int = lambda: int(sys.stdin.readline().strip())

def binary_search(trees, left, right, M):
    def possible(trees, length, M):
        count = 0
        for tree in trees:
            count += max(tree-length, 0)
        return count >= M
    
    mid = (left + right) // 2
    if left <= right:
        if possible(trees, mid, M):
            return max(mid, binary_search(trees, mid + 1, right, M))
        else:
            return binary_search(trees, left, mid - 1, M)
    else:
        return right

def solution():
    N, M = get_line()
    trees = list(get_line())
    print(binary_search(trees, 0, max(trees), M))
    
if __name__ == "__main__":
    solution()