class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        length = len(s)
        idx=0
        size= len(spaces)
        idx2=0
        ans=""
        while idx2 < length:
            if idx < size:
                if idx2 == spaces[idx]:
                    ans += " "
                    idx+=1
                
            ans += s[idx2]
            idx2+=1
        
        return ans