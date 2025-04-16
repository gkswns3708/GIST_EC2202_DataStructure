class Node:
  def __init__(self,key=None, next=None):
    self.key=key
    self.next=next

class SingleLinkedList:
  def __init__(self):
    self.head = None
    self.size = 0
    self.tail = None

  def pushFront(self, key):  # O(1)
    new_node =Node(key)
    new_node.next = self.head
    self.head = new_node
    self.size += 1
    if self.size == 1:
      self.tail = self.head

  def pushBack(self, key):  # O(1) using self.tail
    new_node=Node(key)
    if self.size == 0:
      self.head=new_node
      self.next= None
    else:
      node=self.head
      while node.next != None:
        node = node.next
      node.next = new_node
    self.size +=1


  def popFront(self):                     # O(1)
    if self.size == 0:
      return None
    else:
      key = self.head.key
      self.head = self.head.next
      self.size -= 1
      if self.size == 0:
        self.tail = None
      return key

  def popBack(self):
    if self.size == 0:
      return None
    else:
      prev = None
      tail = self.head
      while tail.next != None:
        prev = tail
        tail = tail.next
      key = tail.key

      if self.size == 0:
        self.head = None
      else:
        prev.next = None
      self.size -= 1
      return key

  def search(self,key):
    node = self.head
    while node != None:
      if node.key == key:
        return node
      else:
        node = node.next
    return None


  def __iter__(self):
    node = self.head
    while node:
      yield node
      node = node.next


  def __str__(self):
    return "->".join([str(node) for node in self])

  def insert(self, k, key):
    node = self.head
    new_node = Node(key)
    if self.size <= k:
      self.pushBack(key)
    else:
      for i in range(k-1):
        node = node.next
      new_node.next = node.next
      node.next = new_node
      self.size += 1