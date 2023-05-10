class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = defaultdict(int)
        outdegree = defaultdict(list)
        
        for end , start in prerequisites:
            outdegree[start].append(end)
            indegree[end] += 1
        
        queue = deque()
        for i in range(numCourses):
            if i not in indegree:
                queue.append(i)
        temp = []
        while queue:
            vertix = queue.popleft()
            temp.append(vertix)
            for val in outdegree[vertix]:
                indegree[val] -= 1
                if indegree[val] == 0:
                    queue.append(val)
        
        if len(temp) != numCourses:
            return False
        
        return True