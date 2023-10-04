class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        ans = []
        
        graph = defaultdict(list)
        for start , end in prerequisites:
            graph[start].append([end , 1])
        
        
        def shortestPath(start , destination):
            distances = {node : float('inf')  for node in range( numCourses)}
            distances[start] = 0
            
            heap = [(0 , start)]
            while heap:
                distance , node = heap.pop()
                for end , width in graph[node]:
                    newDistance = distance + width

                    if distances[end] > newDistance:
                        heappush(heap , [newDistance , end])
                        distances[end] = newDistance
            
            ans = False
            if distances[destination] != float('inf'):
                ans = True
            return ans
            
        for start , end in queries:
            ans.append(shortestPath(start  , end))
        
        return ans