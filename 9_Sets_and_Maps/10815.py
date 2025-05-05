import sys
class Entry:
    def __init__(self, key, value):
        self.key = key
        self.value = value

class Dict():
    def __init__(self, length):
        self.data = [None]  * length
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
            return True # Modified
        else:
            return False # Modified
        
if __name__ == "__main__":
    N = int(sys.stdin.readline())
    d = Dict(1000003)
    for num in sys.stdin.readline().split():
        d[num] = True
    M = int(sys.stdin.readline())
    for num in sys.stdin.readline().split():
        if d[num]:
            print(1)
        else:
            print(0)