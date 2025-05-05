class Entry:
    def __init__(self, key, value):
        self.key = key
        self.value = value

class Dict():
    def __init__(self, length):
        self.data = [None]  * length
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