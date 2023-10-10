class Solution:
    def minOperations(self, nums: List[int]) -> int:
        size = len(nums)
        nums = set(nums)
        nums = list(nums)
        nums.sort()
    
        def checker(idx):
            target = nums[idx] + size - 1
            left = idx
            right = len(nums)
            while left + 1 < right:
                mid = left + (right - left)//2
                
                if nums[mid] >= target:
                    right = mid
                else:
                    left = mid
           
            if right == len(nums) or nums[right] != target:
                right -= 1
           
            ans = size - (right - idx + 1)
            
            return ans
        
        ans = size        
        for idx , num in enumerate(nums):
            val = checker(idx)
            ans = min(ans , val)
    
        return ans
            