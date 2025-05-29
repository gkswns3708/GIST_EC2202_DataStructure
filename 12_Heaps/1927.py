class MinHeap:
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
        smallest = i
        l = self.left(i)
        r = self.right(i)

        if l < n and self.A[l] < self.A[smallest]:
            smallest = l
        if r < n and self.A[r] < self.A[smallest]:
            smallest = r
        if smallest != i:
            self.A[i], self.A[smallest] = self.A[smallest], self.A[i]
            self.heapify_down(n, smallest)

    def heapify_up(self, i):
        parent = self.parent(i)
        while i > 0 and self.A[i] < self.A[parent]:
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

    def find_min(self):
        if not self.A:
            return None
        return self.A[0]

    def delete_min(self):
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

n = int(input())
heap = MinHeap()

for _ in range(n):
    x = int(input())
    if x == 0:
        print(heap.delete_min())
    else:
        heap.insert(x)
