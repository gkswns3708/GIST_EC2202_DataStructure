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

if __name__ == "__main__":
    h = MaxHeap()
    
    # Heap은 구조를 유지하기만 하면, 내부 원소의 순서는 변경될 수 있음.
    # 첫번째 Insert Test는 insert-by-insert + heapify_up 방식이고,
    # 아래의 make_heap은 한번에 만든 방식이면서 heapify_down 방식임.
    # 이 맥락에서 정답은 없음. 상황에 맞게 선택하면 된다고 생각함.
    print("== Insert Test ==")
    for x in [2, 8, 6, 1, 10, 15, 3, 12, 11]:
        h.insert(x)
        print("Insert", x, "→", h)

    temp_heap = MaxHeap()
    temp_heap.make_heap([2, 8, 6, 1, 10, 15, 3, 12, 11])
    print("\n== Heapify Test ==")
    print("Heapified:", temp_heap)

    print("\n== Find Max ==")
    print("Max:", h.find_max())  # 최대값 (root)

    print("\n== Delete Max Test ==")
    while len(h) > 0:
        print("Deleted:", h.delete_max(), "→", h)

    print("\n== Make Heap from List ==")
    h.make_heap([4, 8, 6, 1, 10, 15, 3, 12, 11])
    print("Heapified:", h)

    print("Pop all:")
    while len(h) > 0:
        print(h.delete_max(), end=' ')
