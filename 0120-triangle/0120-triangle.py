class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        length = len(triangle)
        for idx in range(1 , length):
            size = len(triangle[idx])
            for i in range(size):
                val = float('inf')
                if i != 0:
                    val = min(val , triangle[idx - 1][i - 1])
                if i != size - 1:
                    val = min(val , triangle[idx - 1][i])
                triangle[idx][i] += val
        
        return min(triangle[-1])
            