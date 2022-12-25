class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        min_position=float('inf')
        min_idx=-1

        for idx,val in enumerate(points):
            x2,y2 = val
            if x==x2 or y==y2:
                position = abs(x2-x) + abs(y-y2)
                if min_position > position:
                    min_position = position
                    min_idx = idx
        
        return min_idx
        
