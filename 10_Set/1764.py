import sys


class Node:
    def __init__(self, key, next=None):
        self.key = key
        self.next = next


class HashSet:
    def __init__(self, size=100):
        self.size = size
        self.data = [None] * size

    def _hash(self, key):
        return hash(key) % self.size

    def add(self, key):
        i = self._hash(key)
        n = self.data[i]
        while n:
            if n.key == key:
                return  # already exists
            n = n.next
        self.data[i] = Node(key, self.data[i])  # prepend

    def remove(self, key):
        i = self._hash(key)
        n = self.data[i]
        if n is None:
            return
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

    def contains(self, key):
        i = self._hash(key)
        n = self.data[i]
        while n:
            if n.key == key:
                return True
            n = n.next
        return False

    def __contains__(self, key):
        return self.contains(key)

    def __str__(self):
        items = []
        for bucket in self.data:
            n = bucket
            while n:
                items.append(n.key)
                n = n.next
        return "{" + ", ".join(map(str, items)) + "}"


if __name__ == "__main__":
    input = sys.stdin.readline
    n, m = map(int, input().split())
    non_seen = HashSet(1000003)
    non_heard = HashSet(1000003)
    for _ in range(n):
        non_heard.add(input().rstrip())
    for _ in range(m):
        non_seen.add(input().rstrip())

    result = []
    for i in range(1000003):
        n = non_heard.data[i]
        while n:
            if n.key in non_seen:
                result.append(n.key)
            n = n.next
    print(len(result))
    for name in sorted(result):
        print(name)
