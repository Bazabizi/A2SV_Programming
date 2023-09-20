class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        left = 0
        ans = float('inf')
        length = len(nums)
        total = 0
        target = sum(nums) - x
        for right in range(length):
            total += nums[right]
            while left <= right and total > target:
                total -= nums[left]
                left += 1
            
            if total == target:
                ans = min(ans , length - (right - left + 1))
        
        if ans==float('inf'):
            ans = -1
        
        return ans