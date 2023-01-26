class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        first = 0
        ans = 1
        length = len(nums)
        
        for idx in range(length):
            if nums[idx] != nums[first]:
                first+=1
                nums[first] = nums[idx]
                ans += 1
        
        return ans