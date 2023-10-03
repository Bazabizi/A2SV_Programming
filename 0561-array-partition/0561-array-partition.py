class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        ans = 0
        length = len(nums)
        for idx in range(0 , length - 1 , 2):
            ans += min(nums[idx] , nums[idx + 1])
        
        return ans