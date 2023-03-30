class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        
        def backtrack(path,find):
            if len(path) == len(nums):
                ans.append(path[:])
                return
            for idx in range(len(nums)):
                if nums[idx] not in find:
                    find.add(nums[idx])
                    path.append(nums[idx])
                    backtrack(path , find)
                    find.remove(nums[idx])
                    path.pop()
            
        backtrack([] , set())
        return ans