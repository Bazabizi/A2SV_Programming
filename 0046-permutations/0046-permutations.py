class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        permutation = []
        
        def backtrack(start):
            if start == len(nums):
                permutation.append(nums[:])
            
            for idx in range(start , len(nums)):
                nums[idx] , nums[start] = nums[start] , nums[idx]
                backtrack(start + 1 )
                nums[idx] , nums[start] = nums[start] , nums[idx]
        
        backtrack(0)
        return permutation