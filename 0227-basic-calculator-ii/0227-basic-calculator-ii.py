import math
from collections import deque

class Solution:
    def calculate(self, s: str) -> int:
        stack = deque()
        num = 0
        operator = "+"
        
        for i in range(len(s)):
            if s[i].isdigit():
                num = num * 10 + int(s[i])
            
            if (not s[i].isdigit() and s[i] != " ") or i == len(s) - 1:
                if operator == "+":
                    stack.append(num)
                elif operator == "-":
                    stack.append(-num)
                elif operator == "*":
                    stack.append(stack.pop() * num)
                elif operator == "/":
                    prev = stack.pop()
                    if prev < 0:
                        stack.append(math.ceil(prev / num))
                    else:
                        stack.append(prev // num)
                
                num = 0
                operator = s[i]
        
        return sum(stack)