class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        ans = set()
        
        def backtrack(idx, current):
            if idx >= len(nums):
                if len(current) >=2:
                    ans.add(tuple(current))
                return
            check = False
            for i in range(idx,len(nums)):
                    num = nums[i]
                    if not current or current[-1] <= num:
                        current.append(num)
                        check = True
                    backtrack(i+1 , current)
                    if check:
                        current.pop()
                        check = False
            backtrack(idx + 1 , current)
        backtrack(0,[])
        return list(ans)