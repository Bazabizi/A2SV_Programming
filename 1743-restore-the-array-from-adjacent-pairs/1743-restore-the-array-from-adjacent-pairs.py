class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        edges = defaultdict(int)
        graph = defaultdict(list)
        
        for start , end in adjacentPairs:
            graph[end].append(start)
            graph[start].append(end)
            edges[start] += 1
            edges[end] += 1
        
        start = 0
        for val in edges:
            if edges[val] == 1:
                start = val
                break
        
        ans = []
        queue = deque([start])
        visited = set([start])
        while queue:
            vertix = queue.popleft()
            ans.append(vertix)
            for val in graph[vertix]:
                if val not in visited:
                    queue.append(val)
                    visited.add(val)
        
        return ans