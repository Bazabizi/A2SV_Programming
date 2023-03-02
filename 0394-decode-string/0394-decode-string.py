class Solution:
    def decode(self, idx,s):
        length  = len(s)
        
        num = ""
        word = ""
        ans = ""
        while idx < length:
            if s[idx] == "]":
                return [ans,idx]
            
            elif s[idx] <= "9" and s[idx] >= "0" :
                num += s[idx]
            
            elif s[idx] == "[":
                num = int(num)
                temp = self.decode(idx + 1 , s) 
                ans += num *(temp[0])
                num = ""
                idx = temp[1]
            else:
                ans += s[idx]
            idx += 1
        
        return ans, idx
        
        
        
    def decodeString(self, s: str) -> str:
        
        ans = self.decode(0,s)
        return ans[0]