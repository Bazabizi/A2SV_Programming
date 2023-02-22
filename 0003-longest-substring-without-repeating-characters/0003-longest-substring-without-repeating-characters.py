class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = 0 
        container = set()
        size = len(s)
        left = 0
        for right in range(size):
            if s[right] in container:
                while left < size and s[left]!=s[right]:
                    container.remove(s[left])
                    left += 1
                    
                left += 1
            
            container.add(s[right])
            ans = max(ans, right-left+1)
        
        return ans