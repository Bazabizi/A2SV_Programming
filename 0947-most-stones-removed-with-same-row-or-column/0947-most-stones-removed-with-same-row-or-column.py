class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        count = defaultdict(int)
        parent = defaultdict(tuple)
        for r  , c in stones:
            parent[(r , c)] = (r , c)
            count[(r , c)] = 1
            
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
        
        for idx1 , (r1 , c1) in enumerate(stones):
            for idx2 , (r2 , c2) in enumerate(stones):
                if idx1 != idx2:
                    if r1 == r2 or c1 == c2:
                        union((r1 , c1) , (r2 , c2))
        
        ans = set()
        for row , col in stones:
            temp = find((row , col))
            ans.add(temp)
        
        return len(stones) - len(ans)