class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
#         n  = len(s)
#         dp = [1]*n
#         dp = defaultdict(str)
#         dp[s[idx]] = 1
#         for idx in range(n):
            
            
#         return max(dp)
        dp = [0] * (27 + 2*k) # since ord('a') = 96
        for c in s:
            index = ord(c) - 96 + k
            # print(index)
            dp[index] = max(dp[index - k : index + k + 1]) + 1
        return max(dp)
