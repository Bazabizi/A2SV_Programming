class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        visited = set()
        graph = defaultdict(list)
        distances = {node:0 for node in range(n)}
        for idx , (s , e) in enumerate(edges):
            graph[s].append(( e , succProb[idx]))
            graph[e].append(( s , succProb[idx]))
        
        heap = [(-1 , start)]
        while heap:
            distance , node = heappop(heap)
            distance = -distance
            if node in visited:
                continue
            visited.add(node)
            
            for child , width in graph[node]:
                newDistance = distance*width
                if newDistance > distances[child]:
                    distances[child] = newDistance
                    heappush(heap , (-newDistance , child))
        
        ans = distances[end]
        return ans