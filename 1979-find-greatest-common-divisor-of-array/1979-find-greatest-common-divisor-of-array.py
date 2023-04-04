class Solution:
    def GCD(self,num1 , num2):
        if num2 ==0:
            return num1
        return self.GCD(num2,num1%num2)
    
    def findGCD(self, nums: List[int]) -> int:
        minVal = min(nums)
        maxVal = max(nums)
        return self.GCD(maxVal , minVal)