class Solution:
    def reverse(self,s,left,right):
        if left >= right:
            return s
        s[left],s[right] = s[right] ,s[left]
        return self.reverse(s,left + 1, right - 1)
    
    
    def reverseString(self, s: List[str]) -> None:
        length = len(s) - 1
    
        return self.reverse(s,0,length)
        
        """
        Do not return anything, modify s in-place instead.
        """
        