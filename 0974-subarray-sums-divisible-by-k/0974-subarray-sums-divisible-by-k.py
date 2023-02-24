class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        prefixCount = defaultdict(int)
        length = len(nums)
        prefixSum  = 0
        ans = 0
        for num in nums:
            prefixSum += num
            if prefixSum % k == 0:
                ans += 1
            if prefixSum % k in prefixCount:
                ans += prefixCount[prefixSum % k]
            prefixCount[prefixSum % k] += 1
            
        return ans