class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        left = 0
        total = 0
        size = len(nums)
        ans = [-1]*size
        for right in range(size):
            total += nums[right]
            
            if right - left == 2*k:
                index = (right + left)//2
                ans[index] = total//(2*k + 1)
                total -= nums[left]
                left += 1
        
        return ans