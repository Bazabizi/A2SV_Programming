class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        word = words[0]
        size = len(words)
        ans =[]
        
        for letter in word:
            check = True
            for idx in range(1,size):
                if letter not in words[idx]:
                    check = False
                    break
                words[idx]=words[idx].replace(letter,"",1)
            if check:
                ans.append(letter)
    
        return ans