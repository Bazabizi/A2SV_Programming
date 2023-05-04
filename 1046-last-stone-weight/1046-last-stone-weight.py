class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        size = len(stones)
        heap = []
        for num in stones:
            heappush(heap , -num)
        
        while size  > 1:
            top = heappop(heap)
            secondtop = heappop(heap)
            if top != secondtop:
                val = top - secondtop
                heappush(heap , val)
                size += 1
            size -= 2
                
        if size:
            return -heap[0]
        
        return  0
        