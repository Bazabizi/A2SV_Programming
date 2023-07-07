class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        size = len(questions)
        dp = [0]*size
        dp[-1] = questions[-1][0]
        for idx in range(size - 2 , -1 , -1):
            val , index = questions[idx]
            dp[idx] += val
            if index + idx + 1 < size:
                dp[idx] += dp[index + idx + 1]
            dp[idx] = max(dp[idx],dp[idx + 1])
        
        return dp[0]