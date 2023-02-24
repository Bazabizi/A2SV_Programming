class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        length  = len(nums)
        prefixSum = [0]*(length + 1)
        
        for start , end in requests:
            prefixSum[start] += 1
            prefixSum[end+1] -= 1
        
        prefixSum = list(accumulate(prefixSum))
        
        nums.sort()
        prefixSum.pop()
        prefixSum.sort()
        ans = 0
        for idx in range(length):
            ans += prefixSum[idx]*nums[idx]
        return ans % (10**9 +7)