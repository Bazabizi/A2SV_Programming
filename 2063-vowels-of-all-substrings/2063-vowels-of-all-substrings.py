class Solution:
    def countVowels(self, word: str) -> int:
        vowels = {'a','e','i','o','u'}
        index = -1
        ans = 0
        n = len(word)
        for idx , l in enumerate(word):
            if l in vowels:
                ans += (idx + 1)* (n - idx)
               
        
        return ans
        