class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for start , end in dislikes:
            graph[start].append(end)
            graph[end].append(start)
        
        visited = defaultdict(int)        
        def dfs(vertix , color):
            visited[vertix] = color
            
            for val in graph[vertix]:
                if val not in visited:
                    
                    if not dfs(val , -color):
                        return False
                else:
                    if visited[val] == color:
                        return False
                
            return True
        
        
        for val in graph:
            if val not in visited:
                if not dfs(val , 1):
                    return False
        
        return True
        
        