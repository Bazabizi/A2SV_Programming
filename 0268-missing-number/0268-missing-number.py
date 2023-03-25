class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        ans = (n**2 + n)//2 - sum(nums)
        
        return ans