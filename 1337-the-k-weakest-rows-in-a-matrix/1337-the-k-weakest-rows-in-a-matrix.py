class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        rank = []
        for idx , arr in enumerate(mat):
            rank.append([arr.count(1) , idx])
        rank.sort()
        
        ans = []
        for idx in range(k):
            ans.append(rank[idx][1])
        
        return ans