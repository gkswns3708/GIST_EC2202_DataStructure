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
            return -1
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
            return -1
        val = self.tail.key
        self.tail = self.tail.prev
        if self.tail:
            self.tail.next = None
        else:
            self.head = None
        self._size -= 1
        return val

    def peek_left(self):
        return self.head.key if self.head else -1

    def peek_right(self):
        return self.tail.key if self.tail else -1

    def is_empty(self):
        return self._size == 0

    def size(self):
        return self._size

if __name__ == "__main__":
    N = list(map(int, sys.stdin.readline().split()))[0]
    deq = Deque()
    for _ in range(N):
        query = list(map(int, sys.stdin.readline().split()))
        # 1 X: 정수 X를 덱의 앞에 넣는다. (1 ≤ X ≤ 100,000)
        # 2 X: 정수 X를 덱의 뒤에 넣는다. (1 ≤ X ≤ 100,000)
        # 3: 덱에 정수가 있다면 맨 앞의 정수를 빼고 출력한다. 없다면 -1을 대신 출력한다.
        # 4: 덱에 정수가 있다면 맨 뒤의 정수를 빼고 출력한다. 없다면 -1을 대신 출력한다.
        # 5: 덱에 들어있는 정수의 개수를 출력한다.
        # 6: 덱이 비어있으면 1, 아니면 0을 출력한다.
        # 7: 덱에 정수가 있다면 맨 앞의 정수를 출력한다. 없다면 -1을 대신 출력한다.
        # 8: 덱에 정수가 있다면 맨 뒤의 정수를 출력한다. 없다면 -1을 대신 출력한다.
        if query[0] == 1: 
            deq.append_left(query[1])
        elif query[0] == 2:
            deq.append_right(query[1])
        elif query[0] == 3:
            print(deq.pop_left())
        elif query[0] == 4:
            print(deq.pop_right())
        elif query[0] == 5:
            print(deq.size())
        elif query[0] == 6:
            print(1 if deq.is_empty() else 0)
        elif query[0] == 7:
            print(deq.peek_left())
        elif query[0] == 8:
            print(deq.peek_right())
        