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

    def is_empty(self):
        return len(self.A) == 0


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
            return None
        key = self.A[0]
        self.A[0] = self.A[-1]
        self.A.pop()
        self.heapify_down(len(self.A), 0)
        return key

    def __str__(self):
        return str(self.A)

    def is_empty(self):
        return len(self.A) == 0


class DualPriorityQueue:
    def __init__(self):
        self.min_heap = MinHeap()
        self.max_heap = MaxHeap()
        self.count = {}

    def insert(self, value):
        self.min_heap.insert(value)
        self.max_heap.insert(value)
        self.count[value] = self.count.get(value, 0) + 1

    def delete_min(self):
        while not self.min_heap.is_empty():
            val = self.min_heap.delete_min()
            if self.count.get(val, 0) > 0:
                self.count[val] -= 1
                break

    def delete_max(self):
        while not self.max_heap.is_empty():
            val = self.max_heap.delete_max()
            if self.count.get(val, 0) > 0:
                self.count[val] -= 1
                break

    def get_max_min(self):
        max_val = None
        min_val = None

        while not self.max_heap.is_empty():
            val = self.max_heap.find_max()
            if self.count.get(val, 0) > 0:
                max_val = val
                break
            else:
                self.max_heap.delete_max()

        while not self.min_heap.is_empty():
            val = self.min_heap.find_min()
            if self.count.get(val, 0) > 0:
                min_val = val
                break
            else:
                self.min_heap.delete_min()

        return (max_val, min_val)


import sys

input = sys.stdin.readline

T = int(input())
for _ in range(T):
    q = DualPriorityQueue()
    k = int(input())
    for _ in range(k):
        cmd, num = input().split()
        num = int(num)
        if cmd == "I":
            q.insert(num)
        elif cmd == "D":
            if num == 1:
                q.delete_max()
            else:
                q.delete_min()

    max_val, min_val = q.get_max_min()
    if max_val is None or min_val is None:
        print("EMPTY")
    else:
        print(f"{max_val} {min_val}")
