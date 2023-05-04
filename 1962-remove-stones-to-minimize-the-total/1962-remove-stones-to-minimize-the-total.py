class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        heap = []
        for num in piles:
            heappush(heap, -num)
        
        while k > 0:
            num = -heappop(heap)
            num -= num //2
            heappush(heap , -num)
            k -= 1
        
        return -sum(heap)