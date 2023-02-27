class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        count = defaultdict(int)
        count[0] = 1
        prefixSum = []
        odd = 0
        ans = 0
        for num in nums:
            if num % 2:
                odd += 1
            prefixSum.append(odd)
        
        for num in prefixSum:
            count[num] += 1
        
        for num in prefixSum:
            if num >= k:
                ans += count[num-k]
        
        return ans