class Node:
  def __init__(self, key):
    self.key = key
    self.next = None
    self.prev = None
    
class Deque:
  def __init__(self):
    self.head = None
    self.tail = None
    self._size = 0

  def append_left(self, key):
    new_node = Node(key)
    if self.head is None:
      self.head = new_node
      self.tail = new_node
    else:
        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node
    self._size += 1

  def append_right(self,key):
    new_node = Node(key)

    if self.tail is None:
      self.head  = new_node
      self.tail = new_node

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
    self._size -=1

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

  def is_empty(self):
    return self._size == 0

def main():
    dq = Deque()

    print("=== append_left / append_right 테스트 ===")
    dq.append_left(10)  # Deque: 10
    dq.append_left(20)  # Deque: 20 10
    dq.append_right(30) # Deque: 20 10 30
    dq.append_right(40) # Deque: 20 10 30 40

    # 순차 출력
    print("현재 Deque 상태 (앞 → 뒤):", end=" ")
    node = dq.head
    while node:
        print(node.key, end=" ")
        node = node.next
    print()  # 기대 결과: 20 10 30 40

    print("현재 Deque 상태 (뒤 → 앞):", end=" ")
    node = dq.tail
    while node:
        print(node.key, end=" ")
        node = node.prev
    print()  # 기대 결과: 40 30 10 20

    print("=== pop_left / pop_right 테스트 ===")
    print("pop_left:", dq.pop_left())   # 20
    print("pop_right:", dq.pop_right()) # 40
    print("pop_left:", dq.pop_left())   # 10
    print("pop_right:", dq.pop_right()) # 30
    print("pop_right (비어있음):", dq.pop_right()) # None + 메시지 출력

    print("=== 최종 상태 확인 ===")
    print("Deque is empty:", dq.is_empty())  # 기대 결과: True

if __name__ == "__main__":
    main()
