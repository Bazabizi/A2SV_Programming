class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        alphabet = set()
        ans = 0
        length = len(s)
        
        for letter in s:
            alphabet.add(letter)
        
        for letter in alphabet:
            count = 0
            left = 0
            for right in range(length):
                if s[right] != letter:
                    count += 1
                
                if count > k:
                    while left < length and s[left] == letter:
                        left +=1
                    left += 1
                    count -= 1
                ans = max(ans , right-left + 1)
        return ans