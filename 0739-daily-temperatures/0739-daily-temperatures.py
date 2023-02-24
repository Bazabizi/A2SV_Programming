class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        length = len(temperatures)
        ans = []
        for index in range(length-1,-1,-1):
            while stack and temperatures[stack[-1]] <= temperatures[index]:
                stack.pop()
            if not stack :
                ans.append(0)
            else:
                ans.append(stack[-1] - index)
            stack.append(index)
        
        return ans[::-1]
                