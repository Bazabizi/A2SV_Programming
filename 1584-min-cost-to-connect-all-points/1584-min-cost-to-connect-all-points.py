class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        size = len(points)
        parent = {i : i for i in range(size)}
        count = {i : 1 for i in range(size)}
        
        def find(child):
            while child != parent[child]:
                parent[child] = parent[parent[child]]
                child = parent[child]
            return child     
        
        def union(x , y):
            rep_x = find(x)
            rep_y = find(y)
            if rep_x != rep_y:
                if count[rep_x] > count[rep_y]:
                    parent[rep_y] = rep_x
                    count[rep_x] += count[rep_y]
                else:
                    parent[rep_x] = rep_y
                    count[rep_y] += count[rep_x]
                return True
            
            return False
        
        temp = []
        for idx1 , (x1 , y1) in enumerate(points):
            for idx2 , (x2 , y2) in enumerate(points):
                if idx1 != idx2:
                    val = abs(x1 - x2) + abs(y1 - y2)
                    temp.append([val , idx1 , idx2])
        temp.sort()
        ans = 0
        for idx , (val ,start , end) in enumerate(temp):
            flag = union(start , end)
            if flag:
                ans += val
        
        return ans