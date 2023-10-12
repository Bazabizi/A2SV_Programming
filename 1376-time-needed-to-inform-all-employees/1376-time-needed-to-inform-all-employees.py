class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        graph = defaultdict(list)
        ans = 0
        for idx , man in enumerate(manager):
            if man != -1:
                graph[man].append(idx)
        
        queue = deque([(headID ,0)])
        while queue:
            vertix , time = queue.popleft()
            if vertix not in graph:
                ans = max(ans , time)
                continue
            
            for child in graph[vertix]:
                queue.append([child , time + informTime[vertix]])
        
        return ans