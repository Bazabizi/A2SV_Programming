class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap =[]
        heapify(heap)
        count =  0
        for num in nums:
            heappush(heap , num)
            count += 1
            if count > k:
                heappop(heap)
                count -= 1
        
        return heap[0]