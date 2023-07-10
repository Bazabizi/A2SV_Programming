class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        size = len(nums)
        dp = defaultdict(lambda: 1)
        for right in range(size):
            for left in range(right):
                val = nums[right] - nums[left]
                dp[(right , val)] = dp[(left , val)] + 1
               
                    
        return max(dp.values())