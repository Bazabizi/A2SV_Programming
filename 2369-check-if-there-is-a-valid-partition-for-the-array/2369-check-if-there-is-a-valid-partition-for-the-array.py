class Solution:
    def validPartition(self, nums: List[int]) -> bool:
        dp = [False]*(len(nums) + 1)
        dp[0] = True
        
        for idx in range(1, len(nums)):
            if nums[idx] == nums[idx - 1]:
                dp[idx + 1] |= dp[idx - 1]
            if idx > 1 and nums[idx] == nums[idx - 1] == nums[idx - 2]:
                dp[idx + 1] |= dp[idx - 2]
            
            if idx > 1 and nums[idx] == nums[idx- 1] + 1 == nums[idx - 2] + 2:
                dp[idx + 1] |= dp[idx - 2]
        # print(dp)
        return dp[-1]