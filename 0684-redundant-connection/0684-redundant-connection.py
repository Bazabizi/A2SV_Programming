class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        size = len(edges)
        parent = { i : i for i in range(1,size + 1)}
        count = {i:1 for i in range(1, size + 1)}
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
                    parent[rep_x] = rep_y
                    count[rep_y] += count[rep_x]
                else:
                    parent[rep_y] = rep_x
                    count[rep_x] += count[rep_y]
        ans = []
        for start , end in edges:
            if find(start) == find(end):
                ans = [start , end]
                break
            union(start , end)
        return ans