class MyCircularQueue:

    def __init__(self, k: int):
        self.queue = [None]*k
        self.front = -1
        self.rear = -1
        self.store = 0
        self.size = k
    def enQueue(self, value: int) -> bool:
        if not self.isFull():
            self.rear += 1
            self.rear %= self.size
            if self.isEmpty():
                self.front = self.rear
            self.queue[self.rear] = value
            self.store += 1    
            # print(self.front, self.rear)
            return True
        return False
    def deQueue(self) -> bool:
        if not self.isEmpty():
            self.front += 1
            self.front %= self.size
            self.store -= 1
            
            # print("deque",self.front ,self.rear)
    
            return True
        return False
    def Front(self) -> int:
        if not self.isEmpty():
            return self.queue[self.front]
        return -1

    def Rear(self) -> int:
        if not self.isEmpty():
            return self.queue[self.rear]
        return -1
        
    def isEmpty(self) -> bool:        
        if self.store == 0:
            return True 
        return False


    def isFull(self) -> bool:
        if self.store == self.size:
            return True 
        return False


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()