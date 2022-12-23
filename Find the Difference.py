class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        newS=""
        check={}
        for i in t:
            check[i] =1+check.get(i,0)
        for i in s:
            if i in check.keys():
                check[i]-=1
        for key,value in check.items():
            if value!=0:
                i=value
                while i>0:
                    newS+=key
                    i-=1
        return newS
