import sys


class Entry:
    def __init__(self, key, value):
        self.key = key
        self.value = value


class Dict:
    def __init__(self, size):
        self.data = [None] * size

    def findkey(self, key):
        i = hash(key) % len(self.data)
        start = i
        while self.data[i] is not None:
            if self.data[i].key == key:
                return (True, i)
            i = (i + 1) % len(self.data)
            if i == start:
                break  # 한 바퀴 돌았으면 종료
        return (False, i)

    def __setitem__(self, key, value):
        found, i = self.findkey(key)
        if found:
            self.data[i].value = value
        else:
            self.data[i] = Entry(key, value)

    def __getitem__(self, key):
        found, i = self.findkey(key)
        if found:
            return self.data[i].value
        else:
            raise KeyError(f"Key '{key}' not found")


if __name__ == "__main__":
    N, M = map(int, sys.stdin.readline().split())
    table_size = 262147
    db = Dict(table_size)

    for _ in range(N):
        site, pw = sys.stdin.readline().strip().split()
        db[site] = pw

    for _ in range(M):
        query = sys.stdin.readline().strip()
        print(db[query])
