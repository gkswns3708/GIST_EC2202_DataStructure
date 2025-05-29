import sys


class Stack:
    def __init__(self):
        self.stack = []  # 내부적으로 리스트 사용
        self.size = 0  # 스택의 크기 관리

    def push(self, x: str):  # 스택에 값 추가
        self.stack.append(x)
        self.size += 1  # 크기 증가

    def pop(self) -> str:  # 스택의 최상단 값 제거 후 반환
        if self.size == 0:
            return -1
        self.size -= 1  # 크기 감소
        return self.stack.pop()

    def get_size(self) -> int:  # 스택의 크기 반환
        return self.size

    def empty(self) -> int:  # 스택이 비어있는지 확인 (비어있으면 1, 아니면 0)
        return 1 if self.size == 0 else 0

    def top(self) -> str:  # 스택의 최상단 값 확인
        if self.size == 0:
            return -1
        return self.stack[-1]


def is_vps(ps: str) -> str:
    stack = Stack()

    for char in ps:
        if char == "(":
            stack.push(char)
        elif char == ")":
            if stack.empty() == 1:  # 스택이 비어있는 경우
                return "NO"
            stack.pop()

    # 모든 연산 후에 스택이 비어있다면 올바른 괄호 문자열
    if stack.empty() == 1:
        return "YES"
    else:
        return "NO"


def main():
    input = sys.stdin.read
    data = input().splitlines()

    T = int(data[0])
    results = []

    for i in range(1, T + 1):
        ps = data[i]
        results.append(is_vps(ps))

    print("\n".join(results))


if __name__ == "__main__":
    main()
