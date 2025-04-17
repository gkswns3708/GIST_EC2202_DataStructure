# BOJ에서는 PyPy3로 제출 시 메모리 초과(스택 메모리 초과로 추정)가 발생합니다.
# PyPy3는 일반적으로 Python3 interpreting 방식보다 메모리 사용량이 적지만만
# PyPy3의 메모리 관리 방식이 Python3와 다르기 때문에 스택 메모리 사용량이 더 많을 수 있습니다.

# Python3로 제출 시 저격 데이터로 인해 무조건적인 [0]번째 원소를 pivot으로 선택하는 코드에 대해 시간초과가 나게 됩니다.
# 이제 19번째 줄 pivot = A[0]에서 pivot = A[len(A) // 2] 같은 다른 원소의 인덱스를 사용하여
# 시간초과를 피할 수 있습니다.


import sys
sys.setrecursionlimit(10**6)

get_line: iter = lambda: map(int, sys.stdin.readline().rstrip().split())
get_input: int = lambda: int(sys.stdin.readline().strip())

def quick_sort(A):
  if len(A) == 0:
    return A

  pivot = A[len(A)// 2] # pivot 0 -> len(A) // 2로 수정
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

