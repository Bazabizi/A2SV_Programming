class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        ans = 0
        prefix = 0
        for idx , num in enumerate(nums):
            prefix += num
            val = math.ceil(prefix/(idx + 1))
            ans = max(ans , val)
        
        return ans