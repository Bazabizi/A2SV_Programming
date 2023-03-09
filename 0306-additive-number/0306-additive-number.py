class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        current = []
        def backtrack(idx):
           
            if idx >= len(num):
                return len(current) >=3
    
            for i in range(idx , len(num)):
            
                string  = str(num[idx:i+1])    
                val = int(str( num[idx : i+1] ) )
                
                if val < 10**(len(string)-1) and len(string) > 1:
                    continue
                
                if len(current) <= 1 or  current[-1] + current[-2] == val:
                    current.append(val)
                    # print(current , idx)
                    if backtrack(i + 1):
                        return True
                    current.pop()
            return False
        
        return backtrack(0)
        