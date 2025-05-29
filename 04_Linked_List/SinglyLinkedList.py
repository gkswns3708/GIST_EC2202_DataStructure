class Node:
    def __init__(self, key=None, next=None):
        self.key = key
        self.next = next


class SingleLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0
        self.tail = None

    def pushFront(self, key):
        new_node = Node(key)
        new_node.next = self.head
        self.head = new_node
        self.size += 1
        if self.size == 1:
            self.tail = self.head

    def pushBack(self, key):
        new_node = Node(key)
        if self.size == 0:
            self.head = new_node
            self.next = None
        else:
            node = self.head
            while node.next != None:
                node = node.next
            node.next = new_node
        self.size += 1

    def popFront(self):
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

    def search(self, key):
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
            for i in range(k - 1):
                node = node.next
            new_node.next = node.next
            node.next = new_node
            self.size += 1


def main():
    sll = SingleLinkedList()

    print("=== pushFront, pushBack 테스트 ===")
    sll.pushFront(10)  # 리스트: 10
    sll.pushFront(20)  # 리스트: 20 -> 10
    sll.pushBack(30)  # 리스트: 20 -> 10 -> 30
    sll.pushBack(40)  # 리스트: 20 -> 10 -> 30 -> 40

    print("현재 리스트:", end=" ")
    for node in sll:
        print(node.key, end=" ")
    print()  # 기대 결과: 20 10 30 40

    print("=== popFront 테스트 ===")
    print("popFront:", sll.popFront())  # 20 제거
    print("현재 리스트:", end=" ")
    for node in sll:
        print(node.key, end=" ")
    print()  # 기대 결과: 10 30 40

    print("=== popBack 테스트 ===")
    print("popBack:", sll.popBack())  # 40 제거
    print("현재 리스트:", end=" ")
    for node in sll:
        print(node.key, end=" ")
    print()  # 기대 결과: 10 30

    print("=== insert(k, key) 테스트 ===")
    sll.insert(1, 15)  # 인덱스 1 뒤에 15 삽입 → 10 -> 15 -> 30
    sll.insert(10, 99)  # 인덱스 10이 초과되므로 pushBack 동작 → 10 -> 15 -> 30 -> 99
    print("현재 리스트:", end=" ")
    for node in sll:
        print(node.key, end=" ")
    print()  # 기대 결과: 10 15 30 99

    print("=== search 테스트 ===")
    target = 30
    found_node = sll.search(target)
    if found_node:
        print(f"값 {target} 찾음: {found_node.key}")
    else:
        print(f"값 {target} 없음")

    print("=== 최종 리스트 상태 ===")
    print("크기:", sll.size)
    print("내용:", end=" ")
    for node in sll:
        print(node.key, end=" ")
    print()


if __name__ == "__main__":
    main()
