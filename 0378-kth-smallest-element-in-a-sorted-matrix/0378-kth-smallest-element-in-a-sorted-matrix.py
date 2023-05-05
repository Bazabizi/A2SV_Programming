class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        length = len(matrix)
        heap = []
        def inbound(row , col):
            return 0 <= row < len(matrix) and  0 <= col < len(matrix)
            
        for row in range(length):
            heappush(heap , (matrix[row][0] ,(row , 0)))
            
        ans = heap[0]
        count = 0
        while count < k:
            if heap:
                val , direction = heappop(heap)
            count += 1
            row , col = direction
            ans = val
            
            if inbound(row , col + 1):
                heappush(heap , (matrix[row][col + 1] ,(row , col + 1)))
        
        return ans