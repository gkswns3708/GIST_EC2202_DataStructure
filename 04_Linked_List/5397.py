import sys
 
class Node:
    def __init__(self, data=None):
        self.data = data
        self.prev = None
        self.next = None
        
class LinkedList: # 이런식으로 Customize한 Linked List 사용 가능.
    def __init__(self):
        self.head = Node()          # 더미 헤드 노드
        self.cursor = self.head     # 커서는 헤드에 저장
 
    def insert(self, data):
        new_node = Node(data)
        new_node.prev = self.cursor
        new_node.next = self.cursor.next
 
        if self.cursor.next:
            self.cursor.next.prev = new_node
        
        self.cursor.next = new_node
        self.cursor = new_node
    
    def delete(self):
        if self.cursor is not self.head:    # 헤드에서는 삭제 불가
            self.cursor.prev.next = self.cursor.next
            if self.cursor.next:
                self.cursor.next.prev = self.cursor.prev
            self.cursor = self.cursor.prev  # 삭제 후 커서 왼쪽으로 이동
    
    def move_left(self):
        if self.cursor is not self.head:
            self.cursor = self.cursor.prev
 
    def move_right(self):
        if self.cursor.next:
            self.cursor = self.cursor.next
 
    def get_result(self):
        result = []
        current = self.head.next
 
        while current:
            result.append(current.data)
            current = current.next
 
        return ''.join(result)
 
def main():     
    input = sys.stdin.readline   
    t = int(input())
    for _ in range(t):
        linked_list = LinkedList()
        
        for c in input().rstrip():
            if c == '-':
                linked_list.delete()
            elif c == '<':
                linked_list.move_left()
            elif c == '>':
                linked_list.move_right()
            else:
                linked_list.insert(c)
        
        print(linked_list.get_result())
 
if __name__ == '__main__':
    main()