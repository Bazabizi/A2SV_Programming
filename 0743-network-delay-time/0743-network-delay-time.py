class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        distances = {node : float('inf')  for node in range(1 , n + 1)}
        distances[k] = 0
        graph = defaultdict(list)
        
        for start , end , width in times:
            graph[start].append([end , width])
        
        heap = [(0 , k)]
        while heap:
            distance , node = heap.pop()
            for end , width in graph[node]:
                newDistance = distance + width
                
                if distances[end] > newDistance:
                    heappush(heap , [newDistance , end])
                    distances[end] = newDistance
        
        ans = -1
        val = max(distances.values())
        if val != float('inf'):
            ans = val
        return ans
                    