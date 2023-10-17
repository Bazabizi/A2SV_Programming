class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        length = len(nums)
        dp = [1]*length
        counter = [1]*length
        
        for idx in range(length):
            for idx2 in range(idx - 1 , -1 , -1):
                if nums[idx] > nums[idx2]:
                    if dp[idx2] >= dp[idx]:
                        dp[idx] = dp[idx2] + 1
                        counter[idx] = 0
                    if dp[idx2] + 1 == dp[idx]:
                        counter[idx] += counter[idx2]
        max_length = max(dp)
        ans = 0
        
        for idx , num in enumerate(dp):
            if num == max_length:
                ans += counter[idx]
        
        return ans