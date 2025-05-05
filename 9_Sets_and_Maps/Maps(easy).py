class Dict():
    def __init__(self):
        self.data = []
    def __len__(self):
        return len(self.data)
    def __setitems__(self, K, value):
        i = self.findkey(K)
        if i >=0:
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
        
            