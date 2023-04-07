class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        ans = 0
        count = defaultdict(set)
        
        for start , end in roads:
            count[start].add(end)
            count[end].add(start)
        
        for city in range(n):
            for city2 in range(city + 1 , n):
                rank = len(count[city]) + len(count[city2])
                if city in count[city2]:
                    rank -= 1
            
                ans = max(rank , ans)
            
        return ans