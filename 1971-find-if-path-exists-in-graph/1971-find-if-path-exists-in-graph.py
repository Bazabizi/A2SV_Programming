class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        parent = { i : i for i in range(n)}
        count = {i:1 for i in range(n)}
        def find(child ):
            if child == parent[child]:
                return child
            parent[child] = find(parent[child])
            
            return parent[child]
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
        for start , end in edges:
            union(start , end)
        
        return find(source) == find(destination)
