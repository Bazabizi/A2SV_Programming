class Solution:
    def longestAlternatingSubarray(self, nums: List[int], threshold: int) -> int:
        length = len(nums)
        left = 0
        ans = 0
        
        for right in range(length):
            
            while left < length and( nums[left] %2 or nums[left] > threshold):
                left += 1
            if right > 0:
                if right > left and (nums[right] % 2 == nums[right - 1] %2 or nums[right] > threshold):
                    left = right
                else:
                    ans = max(ans , right - left + 1)
            else:
                ans = max(ans , right - left + 1)
        return ans