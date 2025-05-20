import sys
sys.setrecursionlimit(10**9)
get_line: iter = lambda: map(int, sys.stdin.readline().rstrip().split())
get_input: int = lambda: int(sys.stdin.readline().strip())

def bubble_sort(A):
  if len(A) == 0:
    return A

  for i in range(len(A)-1):
    if A[i] > A[i+1]:
      A[i], A[i+1] = A[i+1], A[i]

  return bubble_sort(A[:-1]) + [A[-1]]

def solution():
    n = get_input()
    ws = []
    for i in range(n):
        ws.append(get_input())
    ws = bubble_sort(ws)
    for i in ws:
        print(i)

if __name__ == "__main__":
    solution()