class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        
        ans = 0
        indegree = defaultdict(int)
        graph = defaultdict(list)
        for start , end in edges:
            graph[start].append(end)
            graph[end].append(start)
            indegree[start] += 1
            indegree[end] += 1
        sums = defaultdict(int)
        for idx , val in enumerate(values):
            sums[idx] = val
        
        queue = deque()
        for num in range(n):
            if indegree[num] < 2:
                queue.append(num)
        
        while queue:
            vertix = queue.popleft()
            if sums[vertix] %k == 0:
                ans += 1
            
            for child in graph[vertix]:
                indegree[child] -= 1
                sums[child] += sums[vertix]
                if indegree[child] == 1:
                    queue.append(child)
        
        return ans