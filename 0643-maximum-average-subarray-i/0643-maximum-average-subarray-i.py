class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        length = len(nums) 
        ans = -(10**4)
        total = 0
        left = 0
        
        for right in range(length):
            total += nums[right]
            if right- left == k:
                total -= nums[left]
                left += 1
            
            if right -left +1 == k:
                average = total / k
                ans = max(ans,average)
        
        return ans