class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        idx_odd=0
        size =len(nums)

        for idx in range(size):
            if nums[idx] % 2==0:
                nums[idx_odd] , nums[idx] = nums[idx] , nums[idx_odd]
                idx_odd+=1
                print(nums)
        return nums
