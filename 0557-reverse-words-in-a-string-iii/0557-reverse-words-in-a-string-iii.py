class Solution:
    def reverseWords(self, s: str) -> str:
        arr = s.split()
        ans = ""
        for word in arr:
            ans+=word[::-1]
            ans += " "
        ans = ans[:-1]
        return ans