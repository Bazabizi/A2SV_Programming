class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        length = len(nums)
        ans = length + 1
        left = 0
        total = 0
        
        for right in range(length):
            total += nums[right]
            
            while total >= target and left < length:
                total -= nums[left]
                ans = min( right - left +1 , ans )
                left += 1
        if ans == length + 1:
            return 0
        
        return ans