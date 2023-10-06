class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(list)
        variable = set()

        for idx , (start , end) in enumerate(equations):
            graph[start].append((end , values[idx]))
            graph[end].append((start , 1/values[idx]))
            variable.add(start)
            variable.add(end)
        def dijkstra(src , destination):
            if src not in variable or destination not in variable:
                return -1
            heap = [(1 , src)]
            distance = defaultdict(int)
            distance[src] = 1
            visited = set()
            while heap:
                dis , node = heappop(heap)
                if node in visited:
                    continue
                visited.add(node)
                for end , width in graph[node]:
                    val = dis * width
                    distance[end] = val
                    heappush(heap , (val , end))
            
            res = -1
            if destination in distance:
                res = distance[destination]
            
            return res
        
        ans = []
        for src , destination in queries:
            val = dijkstra(src , destination)
            ans.append(val)
        
        return ans