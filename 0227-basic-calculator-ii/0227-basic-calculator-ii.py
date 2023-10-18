class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        arr = [0]*(10**4)
        arr2 = [0]*(10**4)
        
        for num in s:
            if num == " ":
                continue
            if not stack:
                stack.append(int(num))
                continue
            val = num    
            if '0' <= num <= '9':
                val = int(num)
                if str(stack[-1]).isdigit():
                    val = stack.pop() *10 + int(num)
            stack.append(val)
        stack2 = stack.copy()
        stack = []
        idx = 0
        while idx  < len(stack2):
            val = stack2[idx]
            if val != "+" and val != "*" and val != "/" and val != "-":
                stack.append(val)
                idx += 1
                continue
            if val == "+":
                
                idx += 1
                continue
            if val == "-":
                stack.append(-stack2[idx + 1])
                idx += 2
                continue
            if val == "/" or val == "*":
                num = stack.pop()
                if val == "/":
                    num /= stack2[idx + 1]
                    if num < 0:
                        num = math.ceil(num)
                    num = math.floor(num)
                else:
                    num *= stack2[idx + 1]
                idx += 2
                stack.append(num)
                continue
        
        return sum(stack)