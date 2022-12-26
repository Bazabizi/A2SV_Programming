class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        size=len(nums)
        for val in range(size+1):
            if not val in nums:
                return val