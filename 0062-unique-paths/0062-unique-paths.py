class Solution:
    def __init__(self):
        self.memo = defaultdict(int)
        
    def inbound(self,row , col):
        return row > 0 and col > 0
    def uniquePaths(self, m: int, n: int) -> int:
        if m == 1 and n == 1:
            return 1
        
        if (m , n) in self.memo:
            return self.memo[(m , n)]
        
        if self.inbound(m - 1 , n):
            self.memo[(m , n)] += self.uniquePaths(m -1 , n)
        
        if self.inbound(m  , n - 1):
            self.memo[(m , n)] += self.uniquePaths(m  , n - 1)
        
        return self.memo[(m , n)]