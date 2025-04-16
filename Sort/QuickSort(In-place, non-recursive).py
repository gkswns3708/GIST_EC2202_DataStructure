import random

# partition range a[lo:hi+1] and return index of pivot
def partition(a, lo, hi):
  p = (lo + hi)//2
  pivot = a[p]
  a[p] = a[hi]  # Swap pivot with last item
  a[hi] = pivot

  i = lo - 1
  j = hi
  while i < j:
    i += 1
    while a[i] < pivot:
      i += 1
    j -= 1
    while a[j] > pivot and j > lo:
      j -= 1
    if i < j:
      t = a[i]; a[i] = a[j]; a[j] = t  # swap a[i] and a[j]
  a[hi] = a[i]
  a[i] = pivot # Put pivot where it belongs
  return i     # index of pivot

# sort range a[lo:hi+1]
def quick_sort(a, lo, hi):
  if (lo < hi):
    pivot = partition(a, lo, hi)
    quick_sort(a, lo, pivot - 1)
    quick_sort(a, pivot  + 1, hi)


n = 10000
w = [random.randrange(1000000) for _ in range(n)]
print(w[:100])
quick_sort(w, 0, n - 1) # in-place
print(w[:100])
