class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = set()
        candidates.sort()
        def backtrack(target , total , path , idx):
            if total == target:
                temp = sorted(path)
                ans.add(tuple(temp))
                
                return
            if total > target or idx >= len(candidates):
                return
            
            for i in range(idx , len(candidates)):
                if i > idx and candidates[i] == candidates[i - 1]:
                    continue
                if total + candidates[i]> target:
                    return
                path.append(candidates[i])
                backtrack(target , total + candidates[i], path , i + 1)
                path.pop()
        backtrack(target , 0 , [] , 0)
        res = []
        for val in ans:
            res.append(list(val))
        
        return res
            