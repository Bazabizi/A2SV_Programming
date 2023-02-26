class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        ans = 0
        stack = []
        flag = False
        for parentheses in s:
            if parentheses =="(":
                stack.append(parentheses)
                flag = True
            else:
                if flag:
                    ans += 2**(len(stack)-1)
                    flag = False 
                stack.pop()
        return ans
                    