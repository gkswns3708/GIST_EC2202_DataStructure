class Entry:
    def __init__(self, key, value):
        self.key = key
        self.value = value


class Dict:
    def __init__(self, length):
        self.data = [None] * length

    def findkey(self, Key):
        # i = f(Key)를 아래와 같이 수정
        start = i = hash(Key) % len(self.data)

        while self.data[i] is not None:
            if self.data[i].key == Key:
                return (True, i)
            i = (i + 1) % len(self.data)
            if i == start:
                break  # 한 바퀴 돌았으면 종료
        return (False, i)

    def __len__(self):
        return len(self.data)

    def __setitem__(self, Key, value):
        found, i = self.findkey(Key)
        if found:
            self.data[i].value = value
        else:
            self.data[i] = Entry(Key, value)

    def __getitem__(self, Key):
        found, i = self.findkey(Key)
        if found:
            return self.data[i].value
        else:
            raise KeyError("Key not found")

    def pop(self, key):
        found, i = self.findkey(key)
        if not found:
            return None

        removed_value = self.data[i].value
        self.data[i] = None

        # 재배치 (linear probing 재구성)
        j = (i + 1) % len(self.data)
        while self.data[j] is not None:
            k = hash(self.data[j].key) % len(self.data)

            # 현재 j에 있는 것을 앞쪽 i로 옮겨도 무방한 경우
            if (i <= j and not (i < k <= j)) or (i > j and not (i < k or k <= j)):
                self.data[i] = self.data[j]
                self.data[j] = None
                i = j

            j = (j + 1) % len(self.data)

        return removed_value


if __name__ == "__main__":
    # 작은 크기의 해시 테이블로 충돌 유도
    d = Dict(5)

    # 삽입 테스트
    d["apple"] = 1
    d["banana"] = 2
    d["cherry"] = 3

    print("Inserted values:")
    print("apple:", d["apple"])
    print("banana:", d["banana"])
    print("cherry:", d["cherry"])

    # 덮어쓰기 테스트
    d["apple"] = 10
    print("\nUpdated 'apple':", d["apple"])

    # 존재하지 않는 키 조회
    try:
        print("\nGet non-existing key:", d["mango"])
    except KeyError as e:
        print("KeyError caught as expected:", e)

    # pop 테스트
    print("\nPopping 'banana':")
    val = d.pop("banana")
    print("Popped value:", val)

    # pop 후 상태 확인
    try:
        print("banana after pop:", d["banana"])
    except KeyError as e:
        print("banana successfully removed. KeyError:", e)

    # 다른 값들이 잘 유지되고 있는지 확인
    print("apple still exists:", d["apple"])
    print("cherry still exists:", d["cherry"])

    # pop non-existent key
    # print("\nPopping non-existent key 'grape':", d.pop("grape"))
    # ======= 충돌 실험 ==========
    # 충돌 실험을 위해 해시 테이블 크기를 아주 작게 잡는다
    d = Dict(3)

    # 해시 충돌 유도: 키들을 직접 설계
    class FixedHashStr(str):
        def __hash__(self):
            return 1  # 모든 key가 동일한 해시값을 가지도록!

    key1 = FixedHashStr("key1")
    key2 = FixedHashStr("key2")
    key3 = FixedHashStr("key3")

    # 서로 다른 key지만 hash % 3 == 1 이 되도록 강제

    print("Inserting colliding keys:")
    d[key1] = "A"
    d[key2] = "B"
    d[key3] = "C"

    print(f"{key1} →", d[key1])
    print(f"{key2} →", d[key2])
    print(f"{key3} →", d[key3])

    print("\nPopping key2:")
    val = d.pop(key2)
    print("Popped value:", val)

    try:
        print("Accessing key2 after pop:", d[key2])
    except KeyError as e:
        print("key2 removed correctly:", e)

    print("Remaining entries:")
    print(f"{key1} →", d[key1])
    print(f"{key3} →", d[key3])
