class Solution:
    def sortVowels(self, s: str) -> str:
        string = []
        vowel = {'a' , 'e' ,'i' , 'o','u'}
        for l in s:
            if l.lower() in vowel:
                heappush(string , l)
        ans = ""
        for l in s:
            if l.lower() in vowel:
                ans += heappop(string)
            else:
                ans += l
        return ans
        