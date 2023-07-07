class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        size = len(questions)
        dp = [0]*size
        maxval = defaultdict(int)
        maxval[size - 1] = questions[-1][0]
        for idx in range(size - 1 , -1 , -1):
            val , index = questions[idx]
            
            dp[idx] += val
            if index + idx + 1 < size:
                dp[idx] += maxval[index + idx + 1]
            maxval[idx] = max(maxval[idx + 1] , dp[idx])
            
        return max(dp)