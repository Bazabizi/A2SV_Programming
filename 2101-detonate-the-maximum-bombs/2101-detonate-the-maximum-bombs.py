class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        ans = 1
        graph = defaultdict(list)
        for idx , (x , y , radius) in enumerate(bombs):
            for idx2,( x1 , y1 , radius2) in enumerate(bombs):
                if idx != idx2 and math.sqrt((x-x1)**2 + (y-y1)**2) <= radius :
                    graph[idx].append(idx2)

        def dfs(vertix , visited):
            visited.add(vertix)
            self.temp += 1
            
            for val in graph[vertix]:
                if val not in visited:
                    dfs(val , visited)
                
        for idx ,val in enumerate(bombs):
            visited = set()
            self.temp = 0
            
            dfs(idx , visited)
            ans = max(self.temp , ans)
        
        return ans
            