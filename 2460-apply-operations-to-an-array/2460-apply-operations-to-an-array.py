class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        size = len(nums)
        
        idx_0 = 0;
        for idx in range(size-1):
            if nums[idx] == nums[idx+1]:
                nums[idx] *=2
                nums[idx+1] = 0
        
        for idx in range(size):
            
            if nums[idx] != 0:
                nums[idx] ,nums[idx_0] = nums[idx_0] , nums[idx]
                idx_0 +=1
                
        return nums