class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = -1
        right = len(nums)
        
        while left + 1 < right:
            mid = left + (right - left) // 2 
            
            if nums[mid] == target:
                return mid
            
            if nums[mid] >= nums[left + 1]:
                if nums[left + 1] <= target < nums[mid]:
                    right = mid
                else:
                    left = mid
            else:
                if target > nums[mid] and target <= nums[right-1]:
                    left = mid
                else:
                    right = mid
        
        return -1
                    
        