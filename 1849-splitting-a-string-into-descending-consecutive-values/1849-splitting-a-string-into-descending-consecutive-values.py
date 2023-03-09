class Solution:
    def splitString(self, s: str) -> bool:
        current = []
        
        def backtrack(idx):
            if idx >= len(s):
                return len(current) >= 2
            
            for i in range(idx,len(s)):
                val = int(str(s[idx :i+1]))
                if len(current) == 0 or current[-1] -1 == val:
                    current.append(val)
                    if backtrack(i + 1):
                        return True
                    current.pop()
            return False
        
        return backtrack(0)
                    