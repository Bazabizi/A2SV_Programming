class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        graph = defaultdict(list)
        row = len(isConnected)
        column = len(isConnected[0])
        for r in range(row):
            for c in range(column):
                if isConnected[r][c] == 1:
                    graph[r].append(c)
        
        self.ans = 0
        visited = set()
        def dfs(vertix, visited):

            visited.add(vertix)
            
            for val in graph[vertix]:
                if val not in visited:
                    dfs(val , visited)
                                    
        
        for r in range(row):
            if r not in visited:
                dfs(r , visited)
                self.ans += 1        
        return self.ans