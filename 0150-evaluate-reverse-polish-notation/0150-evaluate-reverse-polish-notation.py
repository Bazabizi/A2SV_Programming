class Solution:
    def operate(self, num1,num2 , operator) -> int:
        num1= int(num1)
        num2 = int(num2)
        if operator== "+":
            return num1 + num2
        
        elif operator== "/":
            return int(num1 /num2)
        elif operator== "*":
            return num1 * num2
        
        return num1 - num2
    
    
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for value in tokens:
            if value =="*" or value =="+" or value =="-" or value =="/":
                operation = self.operate(stack[-2],stack[-1], value)
                stack.pop()
                stack.pop()
                stack.append(operation)
            else:
                stack.append(int(value))
        return stack[-1]