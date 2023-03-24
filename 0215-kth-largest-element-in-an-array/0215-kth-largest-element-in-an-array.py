class Solution:
    def quickSort(self, nums):
        N = len(nums)
        if N < 2:
            return nums
        
        pivot = nums[N//2]

        left = [l for l in nums if l < pivot]
        mid = [m for m in nums if m == pivot]
        right = [r for r in nums if r > pivot]
        
        return self.quickSort(left) + mid + self.quickSort(right)
    
    
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return self.quickSort(nums)[len(nums) - k]