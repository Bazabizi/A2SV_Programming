class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        graph = defaultdict(list)
        indegree = defaultdict(int)
        for start , end in prerequisites:
            graph[start].append(end)
            indegree[end] += 1
        final = defaultdict(set)    
        queue = deque()
        for i in range(numCourses):
            if i not in indegree:
                queue.append(i)
        ans = [False]*len(queries)
        while queue:
            vertix = queue.popleft()
            for val in graph[vertix]:
                indegree[val] -= 1
                final[val] = final[val].union(final[vertix])
                final[val].add(vertix)
                if indegree[val] == 0:
                    queue.append(val)
        
        for idx , (start , end) in enumerate(queries):
            if start in final[end]:
                ans[idx] = True
        
        return ans