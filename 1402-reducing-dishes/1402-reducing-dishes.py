class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        length = len(satisfaction)
        total = max(satisfaction)
        satisfaction.sort(reverse = True)
        dp = [0]*length
        for idx in range(1 , length):
            dp[idx] += total
            for idx2 in range(idx , -1 , -1):
                dp[idx] += satisfaction[idx2]
            total = dp[idx]
        return max(dp)