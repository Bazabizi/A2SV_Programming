class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap = nums
        heapify(self.heap)
        self.size = len(nums) 
        while self.size > k:
            heappop(self.heap)
            self.size -= 1
        self.k = k

    def add(self, val: int) -> int:
        heappush(self.heap , val)
        self.size += 1
        if self.size > self.k:
            heappop(self.heap)
            self.size -= 1
        
        return self.heap[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)