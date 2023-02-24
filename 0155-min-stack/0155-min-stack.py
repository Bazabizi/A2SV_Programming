class MinStack:

    def __init__(self):
        self.minStack=[]
        self.stack = []
    def push(self, val: int) -> None:
        if self.empty() or self.minStack[-1] >= val:
            self.minStack.append(val)
        self.stack.append(val)
                
    def pop(self) -> None:
        if self.stack[-1]== self.minStack[-1]:
            self.minStack.pop()
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]
        
    def empty(self)->bool:
        if len(self.stack)==0:
            return True
        return False

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()