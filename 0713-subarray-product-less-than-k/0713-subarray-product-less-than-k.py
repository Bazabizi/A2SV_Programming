class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        length = len(nums)
        ans = 0
        left = 0
        product = 1
        for right , num in enumerate(nums):
            product *= num
            
            while product >= k and left <= right:
                product //= nums[left]
                left += 1
                
            ans += right - left + 1
        
        return ans