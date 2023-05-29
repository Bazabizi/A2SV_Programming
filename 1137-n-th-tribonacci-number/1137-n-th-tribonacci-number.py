class Solution:
    def __init__(self):
        self.memory = defaultdict(int)
        
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        if n < 3:
            return 1
        if n not in self.memory:
            self.memory[n] = self.tribonacci(n - 1) + self.tribonacci(n - 2) + self.tribonacci(n - 3)
        
        return self.memory[n]