class Solution:
    def __init__(self):
        self.memo = defaultdict(int)
        
    def fib(self, n: int) -> int:
        if n == 1 :
            return n
        fib1 = 0
        fib2 = 1
        fib3 = 0
        state = 2
        
        while state <= n:
            fib3 = fib1 + fib2
            fib1 = fib2
            fib2 = fib3
            state += 1
        
        return fib3