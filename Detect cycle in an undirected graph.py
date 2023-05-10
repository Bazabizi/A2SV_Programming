from typing import List
from collections import deque
class Solution:
    #Function to detect cycle in an undirected graph.
	def isCycle(self, V: int, adj: List[List[int]]) -> bool:
		#Code here
		visited = set()
		queue = deque()
		for vertix in range(V):
		    if vertix not in visited:
		        queue.append((vertix , -1))
		        visited.add(vertix)
		    while queue:
		        cur , parent = queue.popleft()
		        for val in adj[cur]:
		            if val in visited and val != parent:
		                return 1
		            elif val not in visited:
		                queue.append((val , cur))
                        visited.add(val)
                        
        return 0
