class Solution:
    def rob(self, nums: List[int]) -> int:
        size = len(nums)
        if size == 1:
            return nums[0]
        dp = [0]*(size)
        for idx in range(size - 1 , 0, -1):
            if idx + 2 < size:
                dp[idx] = max(dp[idx] , dp[idx + 2])
            if idx + 3 < size:
                dp[idx] = max(dp[idx] , dp[idx + 3])
            
            dp[idx] += nums[idx]
        
        maxval = max(dp)
        size -= 1
        dp = [0] *(size)
        for idx in range(size - 1, -1, -1):
            
            if idx + 2 < size:
                
                dp[idx] = max(dp[idx] , dp[idx + 2])
            if idx + 3 < size:
                dp[idx] = max(dp[idx] , dp[idx + 3])
            
            dp[idx] += nums[idx]
            
        
        maxval = max(max(dp), maxval)
        return maxval