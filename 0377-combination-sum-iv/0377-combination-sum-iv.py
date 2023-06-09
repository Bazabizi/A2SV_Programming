class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        memo = defaultdict(int)
        def dp(val):
            if val == target:
                return 1
            if val > target :
                return 0
            total = 0
            if val in memo:
                return memo[val]
            for num in nums:
                total += dp(val + num)
            
            memo[val] = total
            return total
        
        return dp(0)