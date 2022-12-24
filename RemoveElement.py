class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        idx_val=0

        for num in nums:
            if num != val:
                nums[idx_val] = num
                idx_val+=1
        print(nums)
        return idx_val

