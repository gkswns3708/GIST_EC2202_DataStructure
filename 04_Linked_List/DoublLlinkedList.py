class Node:
    def __init__(self, key=None):
        self.prev = None
        self.next = None
        self.key = key


class DoublyLinkedList:
    def __init__(self):
        self.head = Node()
        self.tail = Node()

        self.head.next = self.tail
        self.tail.prev = self.head

        self.size = 0

    def splice(self, a, b, x):  # O(1)
        if a is None or b is None or x is None:
            return

        ap = a.prev
        bn = b.next
        xn = x.next

        if ap:
            ap.next = bn
        if bn:
            bn.prev = ap

        a.prev = x
        b.next = xn
        if x:
            x.next = a
        if xn:
            xn.prev = b

    def moveAfter(self, a, x):  # O(1)
        self.splice(a, a, x)

    def moveBefore(self, a, x):  # O(1)
        self.splice(a, a, x.prev)

    def insertAfter(self, x, key):  # O(1)
        new_node = Node(key)
        self.moveAfter(new_node, x)
        self.size += 1

    def insertBefore(self, x, key):  # O(1)
        new_node = Node(key)
        self.moveBefore(new_node, x)
        self.size += 1

    def pushFront(self, key):  # O(1)
        self.insertAfter(self.head, key)

    def pushBack(self, key):  # O(1)
        self.insertBefore(self.tail, key)

    def search(self, key):  # O(n)
        node = self.head.next
        while node != self.tail:
            if node.key == key:
                return node
            node = node.next
        return None

    def remove(self, x):  # O(1)
        if x is None or x == self.head or x == self.tail:
            return None

        x.prev.next = x.next
        x.next.prev = x.prev
        self.size -= 1

    def popFront(self):  # O(1)
        if self.head.next == self.tail:
            return None
        else:
            value = self.head.next.key
            self.remove(self.head.next)
            return value

    def popBack(self):  # O(1)
        if self.head.next == self.tail:
            return None
        else:
            value = self.tail.prev.key
            self.remove(self.tail.prev)
            return value

    def printList(self):
        current = self.head.next
        while current != self.tail:
            print(current.key, end=" ")
            current = current.next
        print()


def main():
    dll = DoublyLinkedList()

    print("=== pushFront, pushBack 테스트 ===")
    dll.pushFront(10)
    dll.pushFront(20)
    dll.pushBack(30)
    dll.pushBack(40)
    dll.printList()  # 기대 결과: 20 10 30 40

    print("=== search & moveAfter 테스트 ===")
    node10 = dll.search(10)
    node40 = dll.search(40)
    if node10 and node40:
        dll.moveAfter(node10, node40)  # 10을 40 뒤로 옮김
    dll.printList()  # 기대 결과: 20 30 40 10

    print("=== moveBefore 테스트 ===")
    node30 = dll.search(30)
    node20 = dll.search(20)
    if node30 and node20:
        dll.moveBefore(node30, node20)  # 30을 20 앞에 옮김
    dll.printList()  # 기대 결과: 30 20 40 10

    print("=== insertBefore, insertAfter 테스트 ===")
    node40 = dll.search(40)
    if node40:
        dll.insertBefore(node40, 35)
        dll.insertAfter(node40, 45)
    dll.printList()  # 기대 결과: 30 20 35 40 45 10

    print("=== popFront, popBack 테스트 ===")
    print("popFront:", dll.popFront())  # 30
    print("popBack:", dll.popBack())  # 10
    dll.printList()  # 기대 결과: 20 35 40 45

    print("=== remove 테스트 ===")
    node35 = dll.search(35)
    dll.remove(node35)
    dll.printList()  # 기대 결과: 20 40 45

    print("=== 리스트 크기 확인 ===")
    print("현재 크기:", dll.size)  # 기대 결과: 3


if __name__ == "__main__":
    main()
