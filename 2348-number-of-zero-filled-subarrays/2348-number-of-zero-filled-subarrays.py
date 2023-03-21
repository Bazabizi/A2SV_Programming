class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        ans = 0
        left = -1
        
        for right , num in enumerate(nums):
            if num != 0:
                left = right
            
            ans += right - left
        return ans