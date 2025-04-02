import sys

class Stack:
    def __init__(self):
        self.stack = []  # 내부적으로 리스트 사용
        self.size = 0  # 스택의 크기 관리
    
    def push(self, x: int):  # 스택에 값 추가
        self.stack.append(x)
        self.size += 1  # 크기 증가
    
    def pop(self) -> int:  # 스택의 최상단 값 제거 후 반환
        if self.size == 0:
            return -1
        self.size -= 1  # 크기 감소
        return self.stack.pop()
    
    def get_size(self) -> int:  # 스택의 크기 반환
        return self.size
    
    def empty(self) -> int:  # 스택이 비어있는지 확인 (비어있으면 1, 아니면 0)
        return 1 if self.size == 0 else 0
    
    def top(self) -> int:  # 스택의 최상단 값 확인
        if self.size == 0:
            return -1
        return self.stack[-1]
    
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
            print(stack.get_size())
        elif command == 4:
            print(stack.empty())
        elif command == 5:
            print(stack.top())
