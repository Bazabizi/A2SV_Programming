class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        queue = deque()
        indegree = defaultdict(int)
        for start , end in edges:
            graph[start].append(end)
            graph[end].append(start)
            indegree[start] += 1
            indegree[end] += 1
        
        for val in range(n):
            if indegree[val] == 1:
                queue.append(val)
        ans = [0]
        while queue:
            size = len(queue)
            temp = []
            for _ in range(size):
                vertix = queue.popleft()
                temp.append(vertix)
                for val in graph[vertix]:
                    indegree[val] -= 1
                    if indegree[val] == 1:
                        queue.append(val)
            ans = temp
        return ans