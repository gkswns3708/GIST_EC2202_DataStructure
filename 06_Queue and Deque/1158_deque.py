import sys

class Node:
    def __init__(self, key):
        self.key = key            
        self.prev = None          
        self.next = None         

class Deque:
    def __init__(self):
        self.head = None         
        self.tail = None         
        self._size = 0          

    def append_left(self, item):
        new_node = Node(item)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self._size += 1

    def append_right(self, item):
        new_node = Node(item)
        if self.tail is None:
            self.head = self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        self._size += 1

    def pop_left(self):
        if self.is_empty():
            print("Deque is empty")
            return None
        val = self.head.key
        self.head = self.head.next
        if self.head:
            self.head.prev = None
        else:
            self.tail = None
        self._size -= 1
        return val

    def pop_right(self):
        if self.is_empty():
            print("Deque is empty")
            return None
        val = self.tail.key
        self.tail = self.tail.prev
        if self.tail:
            self.tail.next = None
        else:
            self.head = None
        self._size -= 1
        return val

    def peek_left(self):
        return self.head.key if self.head else None

    def peek_right(self):
        return self.tail.key if self.tail else None

    def is_empty(self):
        return self._size == 0

    def size(self):
        return self._size

if __name__ == "__main__":
    N, K = map(int, sys.stdin.readline().split())
    dq = Deque()
    for i in range(1, N + 1):
        dq.append_right(i)  
    result = []

    while not dq.is_empty():
        for _ in range(K - 1):
            dq.append_right(dq.pop_left()) 
        result.append(dq.pop_left()) 

    print("<" + ", ".join(map(str, result)) + ">")