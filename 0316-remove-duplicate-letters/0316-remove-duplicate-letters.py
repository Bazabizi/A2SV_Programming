class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        stack = []
        count = defaultdict(int)
        find = set()
        
        for letter in s:
            count[letter] += 1
        
        for letter in s:
            if not stack or (stack[-1] < letter and letter not in find):
                stack.append(letter)
                count[letter] -= 1
                find.add(letter)
            else:
                while stack and  stack[-1] >= letter and count[stack[-1]] > 0 and letter not in find:
                    find.remove(stack[-1])
                    stack.pop()
                if letter not in find:
                    find.add(letter)
                    stack.append(letter)
                count[letter] -= 1
                
        ans="".join(stack)
        
        return ans