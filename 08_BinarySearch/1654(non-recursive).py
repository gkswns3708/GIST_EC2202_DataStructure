import sys
get_line: iter = lambda: map(int, sys.stdin.readline().rstrip().split())
get_input: int = lambda: int(sys.stdin.readline().strip())

def binary_search(lines, N):
    def possible(lines, length, N):
        count = 0
        for line in lines:
            count += line // length
        return count >= N
    left = 1
    right = max(lines)
    result = 0
    while left <= right:
        mid = (left + right) // 2
        if possible(lines, mid, N):
            result = mid
            left = mid + 1
        else:
            right = mid - 1
    return result


def solution():
    K, N = get_line()
    lines = []
    for _ in range(K):
        lines.append(get_input())
    
    print(binary_search(lines, N))

if __name__ == "__main__":
    solution()