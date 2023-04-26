class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        visited = set()
        graph = defaultdict(list)
        for start , end in edges:
            if end not in visited and end != 0:
                graph[start].append(end)
                visited.add(end)
            else:
                graph[end].append(start)
                visited.add(start)
        
        ans = [None]*n
        def dfs(vertix):
            count = Counter()
            for val in graph[vertix]:
                count += dfs(val)
            
            count[labels[vertix]] += 1
            ans[vertix] = count[labels[vertix]]
            return count
            
        dfs(0)
        
        return ans
            