class MaxHeap:
    def __init__(self):
        self.A = []

    def __len__(self):
        return len(self.A)

    def parent(self, i):
        return (i - 1) // 2

    def left(self, i):
        return 2 * i + 1

    def right(self, i):
        return 2 * i + 2

    def heapify_down(self, n, i):
        largest = i
        l = self.left(i)
        r = self.right(i)

        if l < n and self.A[l] > self.A[largest]:
            largest = l
        if r < n and self.A[r] > self.A[largest]:
            largest = r

        if largest != i:
            self.A[i], self.A[largest] = self.A[largest], self.A[i]
            self.heapify_down(n, largest)

    def heapify_up(self, i):
        parent = self.parent(i)
        while i > 0 and self.A[i] > self.A[parent]:
            self.A[i], self.A[parent] = self.A[parent], self.A[i]
            i = parent
            parent = self.parent(i)

    def make_heap(self, arr):
        self.A = arr
        n = len(self.A)
        for i in range(n // 2 - 1, -1, -1):
            self.heapify_down(n, i)

    def insert(self, value):
        self.A.append(value)
        self.heapify_up(len(self.A) - 1)

    def find_max(self):
        if len(self.A) == 0:
            return None
        return self.A[0]

    def delete_max(self):
        if len(self.A) == 0:
            return 0
        key = self.A[0]
        self.A[0] = self.A[-1]
        self.A.pop()
        self.heapify_down(len(self.A), 0)
        return key

    def __str__(self):
        return str(self.A)


import sys

input = sys.stdin.readline

# 문제 풀이 로직
n = int(input())
heap = MaxHeap()
results = []

for _ in range(n):
    x = int(input())
    if x == 0:
        print(heap.delete_max())
    else:
        heap.insert(x)
