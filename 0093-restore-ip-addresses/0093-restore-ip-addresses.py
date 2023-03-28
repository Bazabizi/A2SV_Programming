class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        ans = []
        def backtrack(idx , current , n):
            if idx >= len(s) and n == 4:
                ans.append(".".join(current))
                return 
            if n > 3:
                return
           
            for i in range(idx , len(s)):
                val = s[idx : i+1]
                num = int(val)
                
                if num < 10**(len(val)-1) and len(val) > 1:
                    return
                
                if not current or int(current[-1]) <= 255 and int(val) <= 255 :
                    
                    current.append(val)
                    backtrack(i + 1 , current, n + 1)
                    current.pop() 
        
                if int(val) > 255:
                    return
                
        backtrack( 0 , [] , 0)
        return ans
                
            