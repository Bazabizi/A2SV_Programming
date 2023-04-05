class Solution:
    def minSteps(self, n: int) -> int:
        temp = []
        num = 2
        ans = 0
        
        while num * num <= n:
            while n % num == 0:
                ans += num
                n //= num
            num += 1
        if n > 1:
            ans += n
        
        return ans