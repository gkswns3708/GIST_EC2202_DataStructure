import sys

class Stack:
  def __init__(self):
    self.items = []

  def push(self, val):
    self.items.append(val)

  def pop(self):
    try:                      
      return self.items.pop()
    except IndexError:        
      print("Stack is empty")

  def top(self):
    try:
      return self.items[-1]
    except IndexError:
      print("Stack is empty")

  def __len__(self): 
    return len(self.items)


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
    input = sys.stdin.read
    data = input().splitlines()

    N = int(data[0])  # 알파벳 변수 개수
    expression = data[1]  # 후위 표기법으로 표현된 수식
    alphabet_values = [float(data[i + 2]) for i in range(N)]  # 변수에 대응하는 값들

    result = evaluate_postfix(expression, alphabet_values)
    print(f"{result:.2f}")


if __name__ == "__main__":
    main()
