import sys
class Queue:
    def __init__(self):
        self.items = []           # 빈 리스트로 초기화
        self.front_index = 0      # front 포인터는 0에서 시작

    def enqueue(self, val):
        self.items.append(val)    # 큐에 값 추가

    def dequeue(self):
        # 큐가 비어있는지 확인
        if self.front_index == len(self.items):
            print("Queue is empty")
            return None
        else:
            # optimize_memory()               # (Optional) 메모리 최적화 함수 호출
            x = self.items[self.front_index]  # 현재 front의 아이템 가져오기
            self.front_index += 1             # front 포인터 한 칸 이동
            return x                          # 가져온 아이템 반환
        

if __name__ == "__main__":
    N = int(sys.stdin.readline().rstrip())
    A = list(map(int, sys.stdin.readline().split()))
    B = list(map(int, sys.stdin.readline().split()))
    M = int(sys.stdin.readline().rstrip())
    C = list(map(int, sys.stdin.readline().split()))
    que = Queue()
    for i in range(N):
        if A[i] == 0:
            que.enqueue(B[i])
    que.items.reverse()
    for i in range(M):
        que.enqueue(C[i])
        print(que.dequeue(), end=" ")
            
    
    