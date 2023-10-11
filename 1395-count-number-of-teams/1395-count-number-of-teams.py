class Solution:
    def numTeams(self, rating: List[int]) -> int:
        n = len(rating)
        dp = [[0 , 0] for _ in range(n)]
        ans = 0
        for idx in range(n):
            maxinc = 0
            maxdec = 0
            for j in range(idx - 1,-1,-1):
                if rating[j] < rating[idx]:
                    maxinc += 1
                    ans += dp[j][0]
                if rating[j] > rating[idx]:
                    maxdec += 1
                    ans += dp[j][1]
            
            dp[idx][0] = maxinc
            dp[idx][1] = maxdec
        
        
                
        return ans
        