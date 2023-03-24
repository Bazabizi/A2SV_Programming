class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        size = len(nums)
        idx = 0
        while idx < size:
            if nums[idx] != idx + 1:
                
                if nums[ nums[idx] - 1 ] == nums[idx]:
                    return nums[idx]
                else:
                    idx2 = nums[idx] - 1
                    nums[idx] , nums[idx2] = nums[idx2] , nums[idx] 
                    
            else:
                idx += 1
        