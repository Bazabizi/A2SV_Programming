class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        New_Word=""
        num1=len(word1)
        num2=len(word2)
        fir=0
        sec=0
        while fir<num1 or sec<num2:
            if fir<num1:
                New_Word+= word1[fir]
                fir+=1

            if sec<num2:
                New_Word+= word2[sec]
                sec+=1
        
        return New_Word
