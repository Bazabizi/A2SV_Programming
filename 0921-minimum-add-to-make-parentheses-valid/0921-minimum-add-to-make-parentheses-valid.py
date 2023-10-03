class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        ans = 0
        stack = []
        for l in s:
            if l == "(":
                stack.append('(')
            else:
                if stack:
                    stack.pop()
                else:
                    ans += 1
        
        return ans + len(stack)