class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        dp = defaultdict(int)
        for num in arr[::-1]:
            
            if (num + difference) in dp:
                dp[num] = dp[num + difference] + 1
            else:
                dp[num] = 1
        
        return max(dp.values())