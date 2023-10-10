class Solution:
    def longestObstacleCourseAtEachPosition(self, obstacles: List[int]) -> List[int]:
        
        ans = []
        stack = []
        for num in obstacles:
            if not stack or stack[-1] <= num:
                stack.append(num)
                ans.append(len(stack))
            else:
                index = bisect_left(stack,num + 1)
                ans.append(index + 1)
                stack[index] = num
        
        return ans