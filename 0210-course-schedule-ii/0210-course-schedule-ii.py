class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegree = defaultdict(set)
        outdegree = defaultdict(list)
        queue  = deque()
        visited = set()
        ans = []
        for end   , start  in prerequisites:
            indegree[end].add(start)
            outdegree[start].append(end)
        
        for i in range(numCourses):
            if i not in indegree:
                queue.append(i)
        while queue:
            course = queue.popleft()
            ans.append(course)
            for val in outdegree[course]:
                indegree[val].remove(course)
                if len(indegree[val]) == 0:
                    queue.append(val)
        if len(ans) != numCourses:
            return []
        
        return ans