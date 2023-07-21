class Solution:
    def numDecodings(self, s: str) -> int:
        dp = [0]*len(s)
        length = len(s)
        if s[-1] != "0":
            dp[-1] = 1
        
        for idx in range(length - 2 , - 1 , -1):
            num = s[idx : idx + 2]
            num = int(num)
            if s[idx] == "0":
                continue
            dp[idx] += dp[idx + 1]
            if num < 27:
                if idx != length - 2:               
                    dp[idx] += dp[idx + 2]
                else:
                    dp[idx] += 1
        
        return dp[0]