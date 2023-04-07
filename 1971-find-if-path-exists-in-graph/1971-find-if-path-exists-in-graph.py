class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = defaultdict(set)
        for start , end in edges:
            graph[start].add(end)
            graph[end].add(start)
        
        visited = set()
        def dfs(vertix , visited):
            if vertix == destination:
                return True
            visited.add(vertix)
            
            for edge in graph[vertix]:
                if edge not in visited:
                    found = dfs(edge , visited)
                    if found:
                        return True
            return False
        return dfs(source , visited)