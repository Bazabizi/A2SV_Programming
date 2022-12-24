class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()
        first=strs[0]
        last=strs[-1]
        length = len(strs[0])
           
        while first[:length] != last[:length]:
                length -= 1
                first =first[:length]
        
        return first
