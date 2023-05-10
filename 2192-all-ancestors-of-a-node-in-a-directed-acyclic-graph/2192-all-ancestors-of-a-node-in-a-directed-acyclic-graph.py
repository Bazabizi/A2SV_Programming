class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        graph = defaultdict(list)
        indegree = defaultdict(int)
        for start , end in edges:
            graph[start].append(end)
            indegree[end] += 1
        final = defaultdict(set)    
        queue = deque()
        for i in range(n):
            if i not in indegree:
                queue.append(i)
        ans = []
        while queue:
            vertix = queue.popleft()
            for val in graph[vertix]:
                indegree[val] -= 1
                final[val] = final[val].union(final[vertix])
                final[val].add(vertix)
                if indegree[val] == 0:
                    queue.append(val)
            
        
        for val in range(n):
            arr = sorted(list(final[val]))
            ans.append(arr)
        
        return ans