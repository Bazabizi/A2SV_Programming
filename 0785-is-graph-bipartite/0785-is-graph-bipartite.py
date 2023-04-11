class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        visited = defaultdict(int)
        
        def dfs(visited ,vertix, color):
            visited[vertix] = color
            
            for val in graph[vertix]:
                if val not in visited:
                    if not  dfs(visited , val , -color):
                        return False
                
                else:
                    if visited[val] == visited[vertix]:
                        return False
            
            return True
        
        for idx in range(len(graph)):
            if idx not in visited:
                if not dfs(visited , idx , 1):
                    return False
        
        return True
    