class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = set()
        used = 0
        
        def backtrack(path , idx):
            if idx == len(nums):
                temp = sorted(path)
                res.add(tuple(temp))
                return
            if idx > len(nums):
                return
            path.append(nums[idx])
            backtrack(path, idx + 1)
            path.pop()
            backtrack(path , idx + 1)

        backtrack([] ,0)
        ans = []
        for val in res:
            ans.append(list(val))
        
        return ans