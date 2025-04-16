import sys
get_line: iter = lambda: map(int, sys.stdin.readline().rstrip().split())
get_input: int = lambda: int(sys.stdin.readline().strip())

def binary_search(lines, left, right, N):
    def possible(lines, length, N):
        count = 0
        for line in lines:
            count += line // length
        return count >= N
    
    mid = (left + right) // 2
    if left <= right:
        if possible(lines, mid, N):
            return max(mid, binary_search(lines, mid + 1, right, N))
        else:
            return binary_search(lines, left, mid - 1, N)
    else:
        return right


def solution():
    K, N = get_line()
    lines = []
    for _ in range(K):
        lines.append(get_input())
    
    print(binary_search(lines, 1, max(lines), N))

if __name__ == "__main__":
    solution()