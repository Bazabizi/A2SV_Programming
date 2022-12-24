class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        result=[]
        size=len(points)
        for idx in range(size):
            if points[idx][0]==x or points[idx][1]==y:
                temp = abs( x - points[idx][0]) + abs( y - points[idx][1])
                result.append([temp,idx])
        
        result.sort()
        for val in result:
            ans=val[1]
            return ans
        return -1
        
