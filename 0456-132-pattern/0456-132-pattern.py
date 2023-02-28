class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack =[]
        maxVal = float('-inf')
        size = len(nums)
        for idx in range(size-1,-1,-1):
            if nums[idx] < maxVal:
                return True
            
            while stack and stack[-1] < nums[idx]:
                maxVal = stack.pop()
            
            stack.append(nums[idx])
        
        return False