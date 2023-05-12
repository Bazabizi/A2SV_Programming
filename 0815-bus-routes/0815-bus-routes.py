class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        graph = defaultdict(list)
        for idx , arr in enumerate(routes):
            for val in arr:
                graph[val].append(idx)
        
        queue = deque()
        visited = set()
        for val in graph:
            if val == source:
                queue.append((graph[val] , 1))
                break
        index = set()
        
        while queue:
            
            if target == source:
                return 0
            idx , path = queue.popleft()
            
            for val in idx:
                if val not in index:
                    for route in routes[val]:
                        if route == target:
                            return path
                        if route not in visited:
                            queue.append((graph[route] ,path + 1 ))
                            visited.add(route)
                    index.add(val)
            
        return -1