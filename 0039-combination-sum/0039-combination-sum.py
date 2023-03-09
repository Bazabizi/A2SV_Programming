class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.ans =[]
        def backtrack(idx , arr):
            if sum(arr) == target:
                self.ans.append(arr[:])
                return
            if sum(arr) > target or idx >= len(candidates):
                return
            
            arr.append(candidates[idx])
            backtrack(idx,arr)
            arr.pop()
            backtrack(idx + 1 ,arr)
        
        backtrack(0,[])
        return self.ans