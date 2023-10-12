class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        ans = 0
        for i , (x , y) in enumerate(points):
            count = defaultdict(int)
            for j , (x1 , y1) in enumerate(points[i+1:]):
                slope = 'A'
                if x1 != x:
                    slope = (y1 - y)/(x1 - x)
                count[slope] += 1
                ans = max(count[slope] , ans)
        
        return ans + 1
                