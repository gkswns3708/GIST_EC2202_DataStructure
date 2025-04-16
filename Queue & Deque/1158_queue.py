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
            # optimize_memory()  # (Optional) 메모리 최적화 함수 호출
            x = self.items[self.front_index]  # 현재 front의 아이템 가져오기
            self.front_index += 1             # front 포인터 한 칸 이동
            return x                          # 가져온 아이템 반환

    # Optional: 메모리 누수를 막기 위해 front_index가 전체 크기의 절반이 되면 리스트를 슬라이스
    # def optimize_memory(self):
    #     if self.front_index > len(self.items) // 2:
    #         self.items = self.items[self.front_index:]
    #         self.front_index = 0
            


# 요세푸스 문제 해결 코드
if __name__ == "__main__":
    N, K = map(int, sys.stdin.readline().split())
    q = Queue()
    for i in range(1, N + 1):
        q.enqueue(i)

    result = []
    while not q.front_index == len(q.items):
        # K-1번 회전
        for _ in range(K - 1):
            q.enqueue(q.dequeue())
        result.append(q.dequeue())

    print("<" + ", ".join(map(str, result)) + ">")
