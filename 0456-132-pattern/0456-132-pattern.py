class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack =[]
        maxVal = float('-inf')
        size = len(nums)
        for num in nums[::-1]:
            if num < maxVal:
                return True
            
            while stack and stack[-1] < num:
                maxVal = stack.pop()
            
            stack.append(num)
        
        return False