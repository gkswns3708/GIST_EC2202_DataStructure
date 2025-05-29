class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.parent = None

    def __str__(self):
        return f"Node(key={self.key})"


class BST:
    def __init__(self):
        self.root = None
        self.size = 0

    def __str__(self):
        return f"BST(size={self.size})"

    def find_loc(self, key):
        if self.size == 0:
            return None
        parent = None
        curr = self.root
        while curr:
            if key == curr.key:
                return curr
            elif key < curr.key:
                parent = curr
                curr = curr.left
            else:
                parent = curr
                curr = curr.right
        return parent

    def search(self, key):
        if self.size == 0:
            return None
        node = self.find_loc(key)
        if node and node.key == key:
            return node
        else:
            return None

    def insert(self, key):
        p = self.find_loc(key)
        if p is not None and p.key == key:  # 1) 중복 키 검사
            print("key already exists")
            return None

        n = Node(key)  # 2) 새 노드 생성
        n.parent = p

        if p is None:  # 3) 부모가 없다면(트리 비었으면) → 루트로
            self.root = n

        elif key < p.key:  # 4) 부모가 있으면, 키 비교해서 왼/오른쪽 자식으로 연결
            p.left = n
        else:
            p.right = n

        self.size += 1  # 5) 크기 증가 후 반환
        return n

    def deleteByMerging(self, key):
        # 1) 삭제할 노드 찾기
        x = self.find_loc(key)
        # find_loc은 마지막까지 탐색한 노드를 리턴하므로,
        # 실제 키가 일치하지 않으면 None 처리
        if x is None or x.key != key:
            return None

        # 2) x의 왼쪽·오른쪽 서브트리, 부모 노드 보관
        a = x.left
        b = x.right
        px = x.parent

        # 3) 병합한 서브트리의 루트 c 결정
        if a is None:
            # 왼쪽 서브트리가 없으면 오른쪽 서브트리만 있거나 둘 다 None
            c = b
        else:
            # 왼쪽 서브트리를 기준으로 오른쪽 끝 노드를 찾아
            # 오른쪽 서브트리 b를 연결한 뒤, c = a
            c = a
            m = a
            while m.right:
                m = m.right
            m.right = b
            if b:
                b.parent = m

        # 4) 부모 p에 c를 연결
        if px is None:
            # x가 루트였다면, 새 루트는 c
            self.root = c
            if c:
                c.parent = None
        else:
            if x is px.left:
                px.left = c
            else:
                px.right = c
            if c:
                c.parent = px

        # 5) 트리 크기 갱신, x의 포인터들 끊기
        self.size -= 1
        x.parent = x.left = x.right = None

        return x

    def deleteByCopying(self, key):
        # 1) 삭제할 노드 x 찾기
        x = self.find_loc(key)
        if x is None or x.key != key:
            return None

        # 2) 실제로 삭제(물리적 제거)할 노드(rem) 결정
        # — 자식이 둘 다 있으면 predecessor m을 물리 제거
        if x.left and x.right:
            # 2-1) predecessor 찾기: 왼쪽 서브트리에서 가장 큰 노드
            m = x.left
            while m.right:
                m = m.right
            # 2-2) x.key에 m.key 복사
            x.key = m.key
            # 2-3) 이제 m(최대 노드)은 오른쪽 자식이 없으므로,
            #       m.left (있으면)만 부모에 붙이고 m을 삭제
            rem = m
            child = m.left
            pm = m.parent
            if child:
                child.parent = pm
            if pm.left is m:
                pm.left = child
            else:
                pm.right = child

        # — 자식이 하나 이하이면 그 노드 x를 바로 제거
        else:
            rem = x
            child = x.left if x.left else x.right
            px = x.parent
            if px is None:
                # x가 루트인 경우
                self.root = child
                if child:
                    child.parent = None
            else:
                if px.left is x:
                    px.left = child
                else:
                    px.right = child
                if child:
                    child.parent = px

        # 3) 크기 감소, 삭제된 노드 포인터 초기화
        self.size -= 1
        rem.parent = rem.left = rem.right = None

        # 4) 삭제된 노드 반환
        return rem

    def max_node(self, start_node=None):
        """
        start_node로부터 시작해서 가장 오른쪽 끝(최대) 노드를 리턴.
        start_node가 None이면 self.root에서 시작.
        """
        node = start_node if start_node is not None else self.root
        if node is None:
            return None
        while node.right:
            node = node.right
        return node

    def preorder(self):
        """루트→왼쪽→오른쪽 순으로 방문한 키의 리스트를 반환"""
        result = []

        def _rec(node):
            if not node:
                return
            result.append(node.key)
            _rec(node.left)
            _rec(node.right)

        _rec(self.root)
        return result

    def inorder(self):
        """왼쪽→루트→오른쪽 순으로 방문한 키의 리스트를 반환"""
        result = []

        def _rec(node):
            if not node:
                return
            _rec(node.left)
            result.append(node.key)
            _rec(node.right)

        _rec(self.root)
        return result

    def postorder(self):
        """왼쪽→오른쪽→루트 순으로 방문한 키의 리스트를 반환"""
        result = []

        def _rec(node):
            if not node:
                return
            _rec(node.left)
            _rec(node.right)
            result.append(node.key)

        _rec(self.root)
        return result


import sys

sys.setrecursionlimit(10**6)


def main():
    bst = BST()
    preorder_input = sys.stdin.read().split()
    for key in map(int, preorder_input):
        bst.insert(key)

    result = bst.postorder()
    for key in result:
        print(key)


if __name__ == "__main__":
    main()
