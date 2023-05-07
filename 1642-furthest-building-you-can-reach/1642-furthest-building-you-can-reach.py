class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        size = len(heights)
        heap = []
        
        for idx in range(size - 1):
            height_difference = heights[idx + 1] - heights[idx]
            if(height_difference > 0):
                heappush(heap , height_difference)
                if len(heap) > ladders:
                    bricks -= heappop(heap)
                if bricks < 0:
                    return idx
        return size - 1