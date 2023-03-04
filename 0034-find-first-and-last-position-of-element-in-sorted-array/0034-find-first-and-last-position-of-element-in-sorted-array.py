class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        ans1 = -1
        left = -1
        right = len(nums)
        while left+1 < right :
            mid = (left + right) // 2
            if nums[mid] >= target:
                right = mid
            else:
                left = mid
        if left != len(nums)-1 and nums[left+1] == target:
            ans1 = left + 1
        
        ans2 = -1
        left = -1
        right = len(nums)
        while left+1 < right :
            mid = (left + right) // 2
            if nums[mid] > target:
                right = mid
            else:
                left = mid
                
        if left != -1 and nums[left] == target:
            ans2 = left
        return ans1,ans2