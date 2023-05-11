class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        self.cycle = -1 
        
        graph = defaultdict(list)
        for start  , end in enumerate(edges):
            if end == -1:
                continue
            graph[start].append(end)
    
        color = defaultdict(int)
        time = defaultdict(int)
        
        def dfs(vertix , path):
            color[vertix] = 1
            
            time[vertix] = path
            
            if vertix in graph:
                for val in graph[vertix]:
                    if color[val] == 2:
                        continue
                    if color[val] == 1:
                        self.cycle  = max(path - time[val] + 1, self.cycle)
                    else:
                        dfs(val , path + 1)

            color[vertix] = 2
            
            return
        
        for val in graph:
            if color[val] == 0:
                dfs(val , 0)
        return self.cycle