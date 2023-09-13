class Solution:
    def longestPalindrome(self, s: str) -> str:
        size = len(s)
        dp = defaultdict(bool)
    
        ans = [0,0]
        
        for i in range(size):
            dp[(i , i)] = True
        
        for idx in range(size - 1):
            if s[idx]==s[idx + 1]:
                ans = [idx , idx + 1]
                dp[(idx , idx + 1)] = True
                ans = [idx , idx + 1]
            else:
                dp[(idx , idx + 1)] = False
                
            
        for idx in range(2 , size):
            start = 0
            end = start + idx
            while end < size:
                if dp[(start + 1,  end-1)] and s[start] == s[end]:
                    ans = [start , end]
                    dp[(start , end)] = True
                else:
                    dp[(start , end)] = False
                start += 1
                end += 1
        
        return s[ans[0] : ans[1]+1]