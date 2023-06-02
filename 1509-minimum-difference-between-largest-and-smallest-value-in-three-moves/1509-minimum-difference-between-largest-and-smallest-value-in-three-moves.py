class Solution:
    def minDifference(self, nums: List[int]) -> int:
        if len(nums) < 5:
            return 0
        size = len(nums)
        nums.sort()
        minval = float('inf')
        for idx in range(4):
            Range = nums[idx - 4] - nums[idx]
            minval = min(minval , Range)
        
        return minval