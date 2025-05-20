import random

def merge(a, b):
  i = 0
  j = 0
  res = []
  while i < len(a) and j < len(b):
    va = a[i]
    vb = b[j]
    if va <= vb:
      res.append(va)
      i += 1
    else:
      res.append(vb)
      j += 1
  # now just copy remaining elements
  # (only one of these can be non-empty)
  res.extend(a[i:])
  res.extend(b[j:])
  return res

def merge_sort(a):
  if len(a) <= 1:
    return a
  mid = len(a) // 2
  left_half = merge_sort(a[:mid])
  right_half = merge_sort(a[mid:])
  return merge(left_half, right_half)

n = 10000
w = [random.randrange(1000000) for _ in range(n)]
print(w[:100])
w = merge_sort(w) 
print(w[:100])