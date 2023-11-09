class Solution:
    def countHomogenous(self, s: str) -> int:
        N = 10**9 +7
        ans = 0
        prev = ""
        count = -1
        for l in s:
            if l != prev:
                ans += (count * (count + 1))//2
                prev = l
                count = 1
                continue
            count += 1
        
        ans += (count * (count + 1))//2
        return ans%N