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
