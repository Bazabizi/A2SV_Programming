class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        size = len(quiet)
        graph = defaultdict(list)
        indegree = defaultdict(int)
        for rich , poor in richer:
            graph[rich].append(poor)
            indegree[poor] += 1
        
        ans = [num for num in range(size)]
        queue = deque()
        for num in range(size):
            if num not in indegree:
                queue.append(num)
        
        while queue:
            rich = queue.popleft()
            
            for val in graph[rich]:
                if quiet[ans[val]] > quiet[ans[rich]]:
                    ans[val] = ans[rich]
                indegree[val] -= 1
                if indegree[val] == 0:
                    queue.append(val)
        
        return ans