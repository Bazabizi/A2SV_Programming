class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        ans = 0
        length = len(nums)
        total = sum(nums)
        for val in range(length + 1):
            ans += val
        ans -= total
        return ans