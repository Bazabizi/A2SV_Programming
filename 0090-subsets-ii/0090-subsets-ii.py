class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = set()
        
        def backtrack(idx ,subset):
            if idx == len(nums):
                temp = subset[:]
                temp.sort()
                ans.add(tuple(temp))
                return 
            
            if idx > len(nums):
                return 
            subset.append(nums[idx])
            backtrack(idx + 1 , subset)
            subset.pop()
            backtrack(idx + 1 , subset)
        
        backtrack( 0 , [])
        ans = list(ans)
        for idx , element in enumerate(ans):
            ans[idx] = list(element)
        
        return ans
            