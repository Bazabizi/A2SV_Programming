class Solution:
    def __init__(self):
        self.memory = defaultdict(int)
        
    def getSum(self,n):
        if n == 0:
            self.memory[0] = 0
            return n
        elif n == 1:
            self.memory[1] = 1
            return 1
        if n in self.memory:
            return self.memory[n]
        if n %2 == 0:
            self.memory[n] = self.getSum(n //2)
        else:
            self.memory[n] = self.getSum((n - 1)//2) + self.getSum(n - (n-1)//2)
        
        return self.memory[n]
    def getMaximumGenerated(self, n: int) -> int:
        for num in range(n + 1):
            self.getSum(num)
        return max(self.memory.values())
    