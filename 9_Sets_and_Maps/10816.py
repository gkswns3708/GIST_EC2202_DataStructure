import sys

class Entry:
    def __init__(self, key, value):
        self.key = key
        self.value = value

class Dict():
    def __init__(self, length):
        self.data = [None] * length

    def findkey(self, Key):
        i = hash(Key) % len(self.data)
        start = i
        while self.data[i] is not None:
            if self.data[i].key == Key:
                return (True, i)
            i = (i + 1) % len(self.data)
            if i == start:
                break
        return (False, i)

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
            return 0  # 없는 키는 0개로 간주

    def increment(self, Key):
        found, i = self.findkey(Key)
        if found:
            self.data[i].value += 1
        else:
            self.data[i] = Entry(Key, 1)

if __name__ == "__main__":
    N = int(input())
    cards = list(map(int, sys.stdin.readline().split()))
    M = int(input())
    queries = list(map(int, sys.stdin.readline().split()))

    # Prime number for hash table size
    # Because the prime number helps to reduce collisions in the hash table
    # and improves the performance of the hash table.
    table_size = 1000003
    counter = Dict(table_size)

    for num in cards:
        counter.increment(num)

    result = []
    for q in queries:
        result.append(str(counter[q]))

    print(' '.join(result))
        