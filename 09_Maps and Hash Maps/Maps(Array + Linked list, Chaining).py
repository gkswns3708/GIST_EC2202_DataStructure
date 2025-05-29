class Node:
    def __init__(self, key, value, next=None):
        self.key = key
        self.value = value
        self.next = next


def hash_function(key):
    return hash(key) % 10


class DictChaining:
    def __init__(self):
        self.data = [None] * 10

    def findkey(self, key):
        i = hash_function(key)
        n = self.data[i]
        while n is not None:
            if n.key == key:
                return n
            n = n.next
        return None

    def __contains__(self, key):
        return self.findkey(key) is not None

    def __getitem__(self, key):
        n = self.findkey(key)
        if n:
            return n.value
        else:
            raise KeyError(key)

    def __setitem__(self, key, value):
        n = self.findkey(key)
        if n:
            n.value = value
        else:
            i = hash_function(key)
            self.data[i] = Node(key, value, self.data[i])  # prepend to the linked list

    def __delitem__(self, key):
        i = hash_function(key)
        n = self.data[i]
        if n is None:
            raise KeyError(key)

        if n.key == key:
            self.data[i] = n.next
            return

        prev = n
        n = n.next
        while n:
            if n.key == key:
                prev.next = n.next
                return
            prev = n
            n = n.next

        raise KeyError(key)

    # 출력용
    def printall(self):
        for i in range(len(self.data)):
            n = self.data[i]
            if n is not None:
                print(f"Index {i}: ", end="")
                while n is not None:
                    print(f"({n.key}, {n.value}) -> ", end="")
                    n = n.next
                print("None")
            else:
                print(f"Index {i}: None")


if __name__ == "__main__":
    d = DictChaining()

    # 삽입
    d["apple"] = 100
    d["banana"] = 200
    d["cherry"] = 300

    # 조회
    print("apple:", d["apple"])  # 100
    print("banana:", d["banana"])  # 200
    print("cherry:", d["cherry"])  # 300
    d.printall()  # 해시 테이블 상태 출력

    # 덮어쓰기
    d["banana"] = 999
    print("banana (updated):", d["banana"])  # 999

    # 삭제
    del d["apple"]
    try:
        print(d["apple"])
    except KeyError as e:
        print("apple removed correctly:", e)

    # 멤버십 테스트
    print("banana in d:", "banana" in d)  # True
    print("apple in d:", "apple" in d)  # False

    # 충돌 유도: 동일한 해시값을 강제로 만드는 객체
    class FixedHashStr(str):
        def __hash__(self):
            return 4  # 모든 키가 같은 해시값을 가지게 함

    k1 = FixedHashStr("key1")
    k2 = FixedHashStr("key2")
    k3 = FixedHashStr("key3")

    d[k1] = "A"
    d[k2] = "B"
    d[k3] = "C"

    print("\n=== 충돌 테스트 ===")
    print(f"{k1} →", d[k1])  # A
    print(f"{k2} →", d[k2])  # B
    print(f"{k3} →", d[k3])  # C

    d.printall()  # 해시 테이블 상태 출력
    # 삭제 테스트
    del d[k2]
    try:
        print(d[k2])
    except KeyError as e:
        print(f"{k2} removed correctly:", e)

    d.printall()  # 해시 테이블 상태 출력

    # 나머지 키는 여전히 유효한지 확인
    print(f"{k1} →", d[k1])
    print(f"{k3} →", d[k3])
