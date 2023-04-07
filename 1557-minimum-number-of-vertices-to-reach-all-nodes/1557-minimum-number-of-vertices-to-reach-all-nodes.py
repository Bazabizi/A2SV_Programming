class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        path = set()
        for start , end in edges:
            path.add(end)
        ans = []
        for vertix in range(n):
            if vertix not in path:
                ans.append(vertix)
        
        return ans