class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums = list(map(str,nums))
        ans = ""
        zero = 0
        for num in nums:
            if num == "0":
                zero +=1
        if zero == len(nums):
            return "0"
        
        nums.sort(reverse=True)
        size =len(nums)
        for idx in range(1,size):
            j = idx-1
            temp = nums[idx]
            
            while j >= 0 and temp + nums[j] > nums[j] + temp:
                nums[j + 1] = nums[j]
                j -=1
            nums[j+1] = temp
                
        ans = "".join(nums)
        return ans