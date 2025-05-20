import sys

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


# 전역 변수 선언
arr = [[0] * 105 for _ in range(105)]
N, K, L = 0, 0, 0

dx = [1, 0, -1, 0]  # 오, 아래, 왼, 위
dy = [0, 1, 0, -1]  # 오, 아래, 왼, 위

poss = True

# DoublyLinkedList로 대체
doublelinkedlist = DoublyLinkedList()  # 뱀의 몸통 정보 (머리부터 꼬리까지)
dirinfo = DoublyLinkedList()  # 방향 전환 정보


def possible(y, x):
    global poss, arr, N
    if 1 <= y <= N and 1 <= x <= N and arr[y][x] != 2:
        return True
    else:
        poss = False
        return False


def move():
    global doublelinkedlist, arr
    head = doublelinkedlist.head.next
    if not head or head.key is None:
        return

    y, x, dir = head.key
    ny, nx = y + dy[dir], x + dx[dir]

    if possible(ny, nx):
        doublelinkedlist.pushFront((ny, nx, dir))


def solved():
    global doublelinkedlist, dirinfo, arr, poss

    doublelinkedlist.pushBack((1, 1, 0))  # 초기 위치
    arr[1][1] = 2  # 뱀 위치 표시
    time = 0

    while poss:
        time += 1
        move()
        head = doublelinkedlist.head.next

        if head:
            y, x, dir = head.key

            if arr[y][x] == 0:
                tail = doublelinkedlist.tail.prev
                if tail:
                    ly, lx, _ = tail.key
                    arr[ly][lx] = 0
                    doublelinkedlist.popBack()

            arr[y][x] = 2

            if dirinfo.size > 0:
                next_dir_info = dirinfo.head.next
                if next_dir_info and time == next_dir_info.key[0]:
                    if next_dir_info.key[1] == 1:
                        dir = (dir + 1) % 4
                    else:
                        dir = (dir + 3) % 4

                    doublelinkedlist.head.next.key = (y, x, dir)
                    dirinfo.popFront()

    return time


def main():
    global N, K, L, arr, dirinfo
    N = int(input())
    K = int(input())
    
    for _ in range(K):
        y, x = map(int, input().split())
        arr[y][x] = 1  # 사과 위치 표시
    
    L = int(input())
    for _ in range(L):
        time, dir = input().split()
        time = int(time)
        if dir == 'L':
            dirinfo.pushBack((time, 0))
        else:
            dirinfo.pushBack((time, 1))
    
    print(solved())


if __name__ == "__main__":
    main()
