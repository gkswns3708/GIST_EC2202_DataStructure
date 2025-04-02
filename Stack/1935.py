class Stack:
    def __init__(self):
        self.stack = []  # 내부적으로 리스트 사용
        self.size = 0  # 스택의 크기 관리
    
    def push(self, x: float):  # 스택에 값 추가
        self.stack.append(x)
        self.size += 1  # 크기 증가
    
    def pop(self) -> float:  # 스택의 최상단 값 제거 후 반환
        if self.size == 0:
            return -1
        self.size -= 1  # 크기 감소
        return self.stack.pop()
    
    def get_size(self) -> int:  # 스택의 크기 반환
        return self.size
    
    def empty(self) -> int:  # 스택이 비어있는지 확인 (비어있으면 1, 아니면 0)
        return 1 if self.size == 0 else 0
    
    def top(self) -> float:  # 스택의 최상단 값 확인
        if self.size == 0:
            return -1
        return self.stack[-1]


def evaluate_postfix(expression: str, alphabet_values: list) -> float:
    s = Stack()
    
    for char in expression:
        # 피연산자인 경우 (A~Z)
        if char.isalpha():
            index = ord(char) - ord('A')
            s.push(alphabet_values[index])
        
        # 연산자인 경우
        elif char in "+-*/":
            a = s.pop()
            b = s.pop()
            
            if char == '+':
                s.push(b + a)
            elif char == '-':
                s.push(b - a)
            elif char == '*':
                s.push(b * a)
            elif char == '/':
                s.push(b / a)
    
    return s.top()


def main():
    import sys
    input = sys.stdin.read
    data = input().splitlines()

    N = int(data[0])  # 알파벳 변수 개수
    expression = data[1]  # 후위 표기법으로 표현된 수식
    alphabet_values = [float(data[i + 2]) for i in range(N)]  # 변수에 대응하는 값들

    result = evaluate_postfix(expression, alphabet_values)
    print(f"{result:.2f}")


if __name__ == "__main__":
    main()
