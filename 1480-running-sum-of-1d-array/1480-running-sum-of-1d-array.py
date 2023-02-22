class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        size = len(nums)
        for idx in range(1,size):
            nums[idx] += nums[idx-1]
        
        return nums