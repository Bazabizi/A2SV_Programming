class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        length = len(nums)
        count =  defaultdict(int)
        ans = 0
        total = 0
        for right in range(length):
            total += nums[right]         
            if total == goal:
                ans += 1
            if total- goal in count:
                ans += count[total-goal]
            count[total] += 1
    
        return ans