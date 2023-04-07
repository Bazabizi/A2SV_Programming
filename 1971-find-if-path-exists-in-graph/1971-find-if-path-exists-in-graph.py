class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = defaultdict(set)
        for start , end in edges:
            graph[start].add(end)
            graph[end].add(start)
        
        visited = set()
        stack = []
        stack.append(source)
        while stack:
            cur = stack.pop()
            if cur == destination:
                return True
            
            visited.add(cur)
            for neighbor in graph[cur]:
                if neighbor not in visited:
                    stack.append(neighbor)
        
        return False