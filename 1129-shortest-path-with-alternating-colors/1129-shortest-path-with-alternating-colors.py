class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        for start , end in redEdges:
            graph[start].append((end , 1))
        
        for start , end in blueEdges:
            graph[start].append((end , -1))
        
        
        visited = set()
        queue = deque([(0,0 , 0)])
        ans  = [-1]*n
        while queue :
            vertix , color ,path = queue.popleft()
            if ans[vertix] == -1:
                ans[vertix] = path

            for val , c in graph[vertix]:
                
                if c != color and (val , c) not in visited:
                    queue.append((val , c , path + 1))
                    visited.add((val , c))
        return ans
        