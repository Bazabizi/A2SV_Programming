class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        length = len(nums)
        sum_ = sum(nums)
        
        target = sum_//2
        if sum_ %2 : return False
        dp = [False]*(target + 1)
        dp[0] = True
        for num in nums:
            for idx in range(target , num - 1, -1):
                dp[idx] |= dp[idx - num]
            
        return dp[target]