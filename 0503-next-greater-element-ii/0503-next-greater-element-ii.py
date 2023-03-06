class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack = []
        temp = [nums[0]]
        ans = [float('inf')]*len(nums)
        for idx , num in enumerate(nums):
            while stack and nums[stack[-1]] < num:
                ans[stack.pop()] = num
                temp.append(num)
            stack.append(idx)
        
        for idx , num in enumerate(ans):
            if num ==float('inf'):
                for val in temp:
                    if val > nums[idx]:
                        ans[idx] = val
                        break
                else:
                    ans[idx] = -1
        
        return ans