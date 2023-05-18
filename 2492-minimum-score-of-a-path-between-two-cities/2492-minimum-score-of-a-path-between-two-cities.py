class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        parent = { i : i for i in range(1,n + 1)}
        score = {i : float('inf') for i in range(1 , n + 1)}
        count = {i:1 for i in range(1, n + 1)}
    
        def find(child):
            while child != parent[child]:
                parent[child] = parent[parent[child]]
                child = parent[child]
            return child     
        
        def union(x , y , val):
            
            rep_x = find(x)
            rep_y = find(y)
            if rep_x != rep_y:
                if count[rep_x] >= count[rep_y]:
                    parent[rep_y] = rep_x
                    score[rep_x] = min(score[rep_x] ,score[rep_y] , val)
                    count[rep_y] += count[rep_x]
                else:
                    parent[rep_x] = rep_y
                    
                    score[rep_y] = min(score[rep_y] ,score[rep_x], val)
                    count[rep_x] += count[rep_y]
            else:
                score[rep_x] = min(score[rep_x] , val)
                
        for start , end , distance in roads:
            union(start , end , distance)
     
        ans = find(1)
        return score[ans]