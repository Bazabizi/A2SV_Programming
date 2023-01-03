class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        size= len(nums)
        ans=[None]*size
        
        for idx in range(size):
            ans[idx] = nums[nums[idx]]
        
        return ans