class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        ans = set()
        
        def backtrack(idx, current):
            if len(current) >=2:
                ans.add(tuple(current))
            if idx >= len(nums):
                return
            check = False
            if not current or current[-1] <= nums[idx]:
                current.append(nums[idx])
                check = True
            backtrack(idx + 1 ,current)
            if check:
                current.pop()
            backtrack(idx + 1 , current)
        
        backtrack(0,[])
        return list(ans)