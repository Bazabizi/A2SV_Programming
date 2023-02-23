class Solution:
    def minWindow(self, s: str, t: str) -> str:
        found = defaultdict(int)
        left = 0
        size = len(s)
        ans=[]
        exists = False
        for letter in t:
            found[letter] += 1
        
        for right in range(size):
            if s[right] in found:
                found[s[right]] -= 1
            
            while max(found.values())==0:
                length = right - left+1
                ans.append([length , left, right])
                exists = True
                if s[left] in found:
                    found[s[left]] +=1
                left += 1
        substring =""
        if exists:
            ans.sort()
            substring = s[ans[0][1]:ans[0][2] +1]
            
        return substring