class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        length = len(nums)
        num = 0
        for val in nums:
            num = num | (1 << val)
        
        for val in range(length + 1):
            if not (num & (1 << val)):
                    return val
        