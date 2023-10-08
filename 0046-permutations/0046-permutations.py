class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        used = 0
        def backtrack(path):
            nonlocal used
            if len(path) == len(nums):
                ans.append(path[:])
                return
            
            for idx in range(len(nums)):
                if used & (1<<idx) == 0:
                    path.append(nums[idx])
                    used |= 1<< idx
                    backtrack(path)
                    path.pop()
                    used ^= 1 << idx
        backtrack([])
    
        return ans