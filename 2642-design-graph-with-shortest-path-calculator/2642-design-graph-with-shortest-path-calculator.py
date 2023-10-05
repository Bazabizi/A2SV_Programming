class Graph:

    def __init__(self, n: int, edges: List[List[int]]):
        self.graph = defaultdict(list)
        for start , end , width in edges:
            self.graph[start].append((end , width))
        self.size = n
    def addEdge(self, edge: List[int]) -> None:
        start , end , width = edge
        self.graph[start].append((end , width))

    def shortestPath(self, node1: int, node2: int) -> int:
        n = self.size
        distances = {node : float('inf') for node in range(n + 1)}
        distances[node1] = 0
        heap = [(0 , node1)]
        visited = set()
        while heap:
            distance , node = heappop(heap)
            if node in visited:
                if node == node2:
                    return distances[node]
                continue
                
            visited.add(node)
        
            for end , width in self.graph[node]:
                newDistance = distance + width
                if newDistance < distances[end]:
                    distances[end] = newDistance
                    heappush(heap , (newDistance , end))
        ans = -1
        if distances[node2] != float('inf'):
            ans = distances[node2]
        return ans

# Your Graph object will be instantiated and called as such:
# obj = Graph(n, edges)
# obj.addEdge(edge)
# param_2 = obj.shortestPath(node1,node2)