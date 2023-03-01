class Solution:
    def reverse(self,s):
        return s[::-1]
    
    def invert(self,s):
        ans = []
        for l in s:
            if l =="0":
                ans.append("1") 
            else:
                ans.append("0")
        return ans    
    
    def binaryString(self,n , k):
        if n == 0:
            return ["0"]
        
        curr = self.binaryString(n-1,k) 
        rev = self.reverse(self.invert(curr))

        return curr + ["1"] + rev
    
    def findKthBit(self, n: int, k: int) -> str:
        ans = self.binaryString(n, k)
        return ans[k-1]
        