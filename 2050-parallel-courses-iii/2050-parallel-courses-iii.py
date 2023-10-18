class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        ans = 0
        graph = defaultdict(list)
        indegree = defaultdict(int)
        times = defaultdict(int)
        for start , end in relations:
            graph[start].append(end)
            indegree[end] += 1
        
        queue = deque()
        for i in range(1 , n+1):
            if i not in indegree:
                queue.append((i , 0))
                
        while queue:
            vertix , t = queue.popleft()
            ans = max(ans , t + time[vertix - 1])
            
            for val in graph[vertix]:
                indegree[val] -= 1
                times[val] = max(times[val] , t + time[vertix - 1])
                if indegree[val] == 0:
                    queue.append([val , times[val]])
        
        return ans