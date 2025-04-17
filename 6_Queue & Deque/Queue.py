class Queue:
    def __init__(self):
        self.items = []          
        self.front_index = 0      

    def enqueue(self, val):
        self.items.append(val)   

    def dequeue(self):
        if self.front_index == len(self.items):
            print("Queue is empty")
            return None
        else:
            x = self.items[self.front_index]  
            self.front_index += 1             
            return x                          

def main():
    q = Queue()

    print("=== enqueue 테스트 ===")
    q.enqueue(10)
    q.enqueue(20)
    q.enqueue(30)
    print("현재 큐 상태:", q.items[q.front_index:])  # 기대 결과: [10, 20, 30]

    print("\n=== dequeue 테스트 ===")
    print("dequeue:", q.dequeue())  # 기대: 10
    print("dequeue:", q.dequeue())  # 기대: 20
    print("현재 큐 상태:", q.items[q.front_index:])  # 기대: [30]

    print("\n=== dequeue 모든 요소 제거 후 상태 ===")
    print("dequeue:", q.dequeue())  # 기대: 30
    print("dequeue (비어 있음):", q.dequeue())  # 기대: None + "Queue is empty"

    print("\n=== enqueue 이후 다시 동작 확인 ===")
    q.enqueue(40)
    q.enqueue(50)
    print("dequeue:", q.dequeue())  # 기대: 40
    print("현재 큐 상태:", q.items[q.front_index:])  # 기대: [50]

if __name__ == "__main__":
    main()
