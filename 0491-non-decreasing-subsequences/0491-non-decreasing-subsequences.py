class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        ans = set()
        
        def backtrack(idx, current):
            if idx >= len(nums):
                if len(current) >=2:
                    ans.add(tuple(current))
                return
            
            if not current or current[-1] <= nums[idx]:
                current.append(nums[idx])
                backtrack(idx + 1 ,current)
                current.pop()
            backtrack(idx + 1 , current)
        
        backtrack(0,[])
        return list(ans)