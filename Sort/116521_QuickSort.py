# BOJ에서는 PyPy3로 제출 시 메모리 초과(스택 메모리 초과로 추정)가 발생합니다.
# PyPy3는 스택 메모리 사용량이 Python3보다 적지만,
# PyPy3의 메모리 관리 방식이 Python3와 다르기 때문에 스택 메모리 사용량이 더 많을 수 있습니다.

# Python3로 제출 시 시간 초과가 발생합니다. 
# 이는 재귀 기반 퀵 정렬(quick sort) 구현에서 깊은 재귀 호출로 인한 스택 사용량 증가와, 
# Python3의 동적 메모리 관리로 인한 함수 호출 오버헤드 때문으로 판단됩니다.
# ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
# In BOJ, submitting with PyPy3 results in memory overflow (presumably due to stack memory overflow).
# Submitting with Python3 results in a time limit exceeded error.
# This is likely due to increased stack usage from deep recursive calls in the quick sort implementation,
# and the function call overhead from Python3's dynamic memory management.


import sys
sys.setrecursionlimit(10**3 * 5)

get_line: iter = lambda: map(int, sys.stdin.readline().rstrip().split())
get_input: int = lambda: int(sys.stdin.readline().strip())

def quick_sort(A):
  if len(A) == 0:
    return A

  pivot = A[0]
  left = []
  right = []
  middle = []

  for a in A:
    if compare(a, pivot) == 1:
      left.append(a)
    elif compare(a, pivot) == 0:
      middle.append(a)
    else:
      right.append(a)

  return quick_sort(left) + middle + quick_sort(right)

def compare(x, y):
    if x[1] > y[1]:
        return -1
    elif x[1] == y[1]:
        if x[0] > y[0]:
            return -1
        elif x[0] == y[0]:
            return 0
        else:
            return 1
    else:
        return 1


N = get_input()
input_arr = []
for _ in range(N):
    a, b = get_line()
    input_arr.append((a, b))

sorted_arr = quick_sort(input_arr)
for i in sorted_arr:
    print(i[0], i[1])

