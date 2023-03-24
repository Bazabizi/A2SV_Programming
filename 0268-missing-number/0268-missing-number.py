class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        size=len(nums)
        if min(nums) == 0:
            for idx in range(size):
                if nums[idx] != 0:
                    while nums[idx] - 1 != idx and nums[idx] != 0 :
                        nums[nums[idx] - 1] , nums[idx] = nums[idx] , nums[nums[idx] - 1]
            
            for num in range(1,size + 1):
                if num != nums[num - 1]:
                    return num
            
        return 0