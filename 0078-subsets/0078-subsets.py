class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.subset = []
        def backtrack(idx , sub):
            if idx  == len(nums):
                self.subset.append(sub[:])
                return
            if idx >= len(nums):
                return 
            sub.append(nums[idx])
            backtrack(idx + 1 , sub)
            sub.pop()
            backtrack(idx + 1 , sub)
        
        backtrack(0,[])
        return self.subset