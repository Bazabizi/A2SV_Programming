class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        length = len(nums)
        prefixSum = 0
        count = defaultdict(int)
        ans = 0
        for index in range(length):
            prefixSum += nums[index]
            if prefixSum == goal:
                ans += 1
            
            if prefixSum - goal in count :
                ans += count[prefixSum - goal]
            
            count[prefixSum] += 1
        return ans