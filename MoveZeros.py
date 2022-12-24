class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        size=len(nums)
        idx_0 = 0
        for idx in range(size):
            if nums[idx]!=0:
                nums[idx] , nums[idx_0] = nums[idx_0] ,nums[idx]
                idx_0 +=1
         
