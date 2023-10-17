class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
#         n  = len(s)
#         dp = [1]*n
#         dp = defaultdict(str)
#         dp[s[idx]] = 1
#         for idx in range(n):
            
            
#         return max(dp)
        dp = [0] * 123 # since ord('a') = 96
        for c in s:
            dp[ord(c)] = max(dp[ord(c) - k : ord(c) + k + 1]) + 1
        return max(dp)
