class Dict:
    def __init__(self):
        self.data = []

    def __len__(self):
        return len(self.data)

    def __setitem__(self, K, value):  # 오타 수정
        i = self.findkey(K)
        if i >= 0:
            self.data[i] = (K, value)
        else:
            self.data.append((K, value))

    def findkey(self, K):
        for i in range(len(self.data)):
            if K == self.data[i][0]:
                return i
        return -1

    def __getitem__(self, K):
        i = self.findkey(K)
        if i >= 0:
            return self.data[i][1]
        else:
            raise KeyError("Key not found")


if __name__ == "__main__":
    d = Dict()

    # 삽입
    d["apple"] = 10
    d["banana"] = 20
    d["cherry"] = 30

    print("apple =", d["apple"])  # 10
    print("banana =", d["banana"])  # 20
    print("cherry =", d["cherry"])  # 30

    # 같은 키에 다른 값을 넣으면 덮어쓰기
    d["banana"] = 99
    print("banana (updated) =", d["banana"])  # 99

    # 없는 키 조회 시 예외 발생
    try:
        print("mango =", d["mango"])
    except KeyError as e:
        print("Error:", e)

    # 길이 확인
    print("Number of keys:", len(d))  # 3 (apple, banana, cherry)
