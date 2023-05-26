class Solution:
    def __init__(self):
        self.memo = defaultdict(int)
    
    def dp(self,idx,nums):
        
        if idx >= len(nums):
            return 0
        if idx == len(nums) - 1 or idx == len(nums) - 2:
            return nums[idx]
        if idx in self.memo:
            return self.memo[idx]
        
        self.memo[idx] = max(self.dp(idx + 2,nums),self.dp(idx + 3,nums)) + nums[idx]
        return self.memo[idx]
        
    def rob(self, nums: List[int]) -> int:
        return max(self.dp(0,nums),self.dp(1,nums))