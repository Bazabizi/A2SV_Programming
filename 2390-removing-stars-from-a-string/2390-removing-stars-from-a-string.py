class Solution:
    def empty(self, stack) -> bool:
        return len(stack) == 0
    
    
    def removeStars(self, s: str) -> str:
        stack = []
        for letter in s:
            if letter != "*":
                stack.append(letter)
            else:
                if not self.empty(stack):
                    stack.pop()
        
        ans = "".join(stack)
        
        return ans