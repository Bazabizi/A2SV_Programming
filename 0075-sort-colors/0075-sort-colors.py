class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zeros = 0
        ones = 0
        twos = 0
        
        for num in nums:
            if num == 1:
                ones += 1
            elif num == 2:
                twos += 1
            else:
                zeros += 1
        idx = 0
        for i in range(zeros):
            nums[idx] = 0
            idx +=1
        for i in range(ones):
            nums[idx] = 1
            idx +=1
        for i in range(twos):
            nums[idx] = 2
            idx +=1
        