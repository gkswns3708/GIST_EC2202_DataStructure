import sys


class Entry:
    def __init__(self, key, value):
        self.key = key
        self.value = value


class Dict:
    def __init__(self, length):
        self.data = [None] * length

    def findkey(self, Key):
        # i = f(Key)를 아래와 같이 수정
        i = hash(Key) % len(self.data)

        while self.data[i] is not None:
            if self.data[i].key == Key:
                return (True, i)
            i = (i + 1) % len(self.data)
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
            return True  # Modified
        else:
            return False  # Modified


if __name__ == "__main__":
    N, M = map(int, sys.stdin.readline().split())
    # Prime number for hash table size
    # Because the prime number helps to reduce collisions in the hash table
    # and improves the performance of the hash table.
    d = Dict(262147)
    for _ in range(N):
        sentence = sys.stdin.readline().strip()
        d[sentence] = True
    cnt = 0
    for _ in range(M):
        sentence = sys.stdin.readline().strip()
        if d[sentence]:
            cnt += 1
        else:
            continue
    print(cnt)
