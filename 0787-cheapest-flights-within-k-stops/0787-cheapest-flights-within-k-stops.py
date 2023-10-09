class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        distances = {node:float('inf') for node in range(n)}
        graph = defaultdict(list)
        for start , end , cost in flights:
            graph[start].append((end , cost))
        # print(graph)
        distances[src] = 0
        heap = []
        heap.append((0 , 0 , src))
        visited = set()
        while heap:
            nodesPassed , distance , node = heappop(heap)
            if nodesPassed >= k + 1:
                continue
           
            for child , width in graph[node]:
                if distances[child] > width + distance and nodesPassed < k + 1 :
                    distances[child] = width + distance
                    heappush(heap , (nodesPassed + 1 , distances[child] , child))
            # print(heap)
        ans = distances[dst]
        if distances[dst] == float('inf'):
            ans = -1
        return ans