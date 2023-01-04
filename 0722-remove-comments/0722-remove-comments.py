class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        code = "\n".join(source)
        temp=""
        size=len(code)
        idx=0
        
        while idx < size:
            if code[idx : idx+2] == "//" :
                
                while idx<size and code[idx] != "\n":
                    idx+= 1
            elif code[idx : idx+2]=="/*":
                idx+=2
                
                while code[idx: idx+2] != "*/":
                    idx +=1
                    
                idx += 2
            else:
                if idx<size :
                    temp += code[idx]
                idx+=1
            
        ans=[]
        length= len(temp)
        idx=0
        
        while idx < length:
            res=""
            
            while idx < length and temp[idx]!="\n" :
                res += temp[idx]
                idx += 1
                
            if len(res)!=0:
                ans.append(res)
            idx +=1
            
        return ans