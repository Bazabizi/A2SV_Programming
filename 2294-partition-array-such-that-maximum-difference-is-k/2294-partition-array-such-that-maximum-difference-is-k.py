class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        nums.sort()
        ans = 1
        left = 0
        
        for right , num  in enumerate(nums):
            if nums[right] - nums[left] > k:
                ans += 1
                left = right
        
        return ans