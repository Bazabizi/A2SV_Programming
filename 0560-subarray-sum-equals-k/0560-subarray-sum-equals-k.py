class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        length = len(nums)
        count =  defaultdict(int)
        ans = 0
        total = 0
        for right in range(length):
            total += nums[right]         
            if total == k:
                ans += 1
            if total- k in count:
                ans += count[total-k]
            count[total] += 1
     
        return ans