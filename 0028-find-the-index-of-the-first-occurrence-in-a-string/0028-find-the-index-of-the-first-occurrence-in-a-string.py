class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        target = 0
        size = len(needle)
        num = size - 1
        left = 0
        total = 0
        if len(haystack) < len(needle):
            return -1
        for idx , l in enumerate(needle):
            target += (ord(l)- 97)*(26**num)
            total += (ord(haystack[idx]) - 97)*(26**num)
            num -= 1
        
        for right in range(size ,len(haystack)):
            if target == total:
                return left
            total -= (26**(size - 1))*(ord(haystack[left]) - ord('a'))
            total *= 26
            total += (ord(haystack[right]) - ord('a') )
           
            left += 1
        if target == total:
                return left
        return -1
            