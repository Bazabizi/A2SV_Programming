class Solution:
    def freqAlphabets(self, s: str) -> str:
        rev=""
        left=0
        right=len(s)
        length=len(s)

        while right>0:
            if s[right-1]=="#":
                num=int(s[right-3:right-1])
                rev += chr(num+96)
                right -=3

            else:
                num =int(s[right-1])
                rev += chr(num+96)
                right -=1
        
        result=""
        n=len(rev)
        for idx in reversed(range(n)):
            result += rev[idx]
        return result
