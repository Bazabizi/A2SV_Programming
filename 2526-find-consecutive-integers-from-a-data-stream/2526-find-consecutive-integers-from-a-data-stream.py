class DataStream:

    def __init__(self, value: int, k: int):
        self.queue = deque()
        self.value = value
        self.target = k
        self.count = 0
    def consec(self, num: int) -> bool:
        if num == self.value:
            self.count += 1
        self.queue.append(num)
        if len(self.queue) > self.target:
            if self.queue[0] == self.value:
                self.count -= 1
            self.queue.popleft()

        if self.count ==self.target:
            return True
        return False


# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)