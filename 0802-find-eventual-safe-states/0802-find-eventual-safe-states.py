class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        colors = [0 for i in range(len(graph))]
        length = len(graph)
        ans = []
        def dfs(vertix):
            if colors[vertix]:
                    return colors[vertix] == 2
                
            if colors[vertix] == 1:
                return False
            
            colors[vertix] = 1
            
            for val in graph[vertix]:
                if not dfs(val):
                    return False
            
            colors[vertix] = 2
            return True
        for idx in range(length):
            if dfs(idx):
                ans.append(idx)  
        
        
        
        return ans