class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        size = len(nums)
        dp = []
        for idx in range(1 , size):
            num = nums[idx - 1] - nums[idx]
            if num != 0:
                dp.append(num)
        
        if not dp:
            return 1
        ans = 2
        
        for idx in range(1 , len(dp)):
            if dp[idx] > 0 and dp[idx - 1] < 0 or dp[idx] < 0 and dp[idx - 1] > 0:
                ans += 1
        
        return ans