class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        prefixSum =[0]
        for num in nums:
            prefixSum.append(num+prefixSum[-1])
        size = len(nums)
        for idx in range(1,size+1):
            if prefixSum[idx-1] == prefixSum[-1]-prefixSum[idx]:
                return idx-1
        
        return -1