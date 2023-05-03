class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapify(nums)
        size = len(nums)
        
        while size > k:
            heappop(nums)
            size -= 1
        return nums[0]