class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        size = len(nums)
        idx = 0
        while idx < size:
            
            # if nums[idx] is in the range of [1,size]
            if nums[idx] > 0 and nums[idx] < size + 1 :
                
                if nums[idx] != idx + 1:
                    if nums[ nums[idx] - 1 ] == nums[idx]:
                        idx += 1
                    else:
                        idx2 = nums[idx] - 1
                        temp = nums[idx]
                        nums[idx] = nums[idx2]
                        nums[idx2] = temp
                else:
                    idx += 1
            else:
                idx += 1
            
        for idx in range(size):
            if nums[idx]!= idx + 1:
                return idx + 1
            
        return size + 1
                