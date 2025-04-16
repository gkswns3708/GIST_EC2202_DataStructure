import sys

class Stack:
    def __init__(self):
        self.stack = []  
    
    def push(self, x):  
        self.stack.append(x) 
    
    def pop(self):  
        if len(self.stack) == 0:
            return -1
        return self.stack.pop()
    
    def top(self):  
        if len(self.stack) == 0:
            return -1
        return self.stack[-1]
    
    def __len__(self): 
        return len(self.stack)

    def empty(self):  
        return 1 if len(self.stack) == 0 else 0
    
    
if __name__ == "__main__":
    get_line = lambda: map(int, sys.stdin.readline().rstrip().split())
    get_input = lambda: int(sys.stdin.readline().strip())

    N = get_input()
    stack = Stack()

    for _ in range(N):
        now_input = list(get_line())
        command = now_input[0]
        
        if command == 1:
            stack.push(now_input[1])
        elif command == 2:
            print(stack.pop())
        elif command == 3:
            print(len(stack))
        elif command == 4:
            print(stack.empty())
        elif command == 5:
            print(stack.top())
