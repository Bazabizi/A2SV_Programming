class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        self.ans = []
        visited = defaultdict(list)
        def dfs(path , vertix):
            
            if vertix == len(graph) - 1:    
                self.ans.append(path[:])
                return
            if not graph[vertix]:
                return
            
            for val in graph[vertix]:
                path.append(val)
                dfs(path , val)
                path.pop()
        
        for idx,visit in enumerate(graph):
            for val in visit:
                visited[val].append(idx)
        
        length = len(graph)
        
        for vertix in range(length):
            if vertix not in visited:
                dfs([vertix] , vertix)
                break
        
        return self.ans