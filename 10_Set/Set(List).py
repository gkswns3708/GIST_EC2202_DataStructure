class SetBasic:
    def __init__(self):
        self.data = []

    def add(self, item):
        if item not in self.data:
            self.data.append(item)

    def remove(self, item):
        if item in self.data:
            self.data.remove(item)

    def contains(self, item):
        return item in self.data

    def __contains__(self, item):  # 'in' 키워드 지원
        return self.contains(item)

    def __len__(self):
        return len(self.data)

    def __str__(self):
        return "{" + ", ".join(map(str, self.data)) + "}"


if __name__ == "__main__":
    print("=== SetBasic 테스트 ===")
    s1 = SetBasic()
    s1.add(10)
    s1.add(20)
    s1.add(30)
    s1.add(10)
    print(s1)  # {10, 20, 30}
    s1.remove(20)
    print(20 in s1)  # False
