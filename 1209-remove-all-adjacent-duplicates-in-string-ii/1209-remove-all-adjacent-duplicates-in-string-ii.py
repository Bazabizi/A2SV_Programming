class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack  = []
        for l in s:
            if not stack or stack[-1][0] != l:
                stack.append([l , 1])
                continue
            if stack[-1][0] == l:
                val = stack[-1][1]
                if val + 1 == k:
                    stack.pop()
                else:
                    stack[-1][1] += 1
            
        
        ans = ""
        for val , duplicate in stack:
            ans += val*duplicate
        return ans