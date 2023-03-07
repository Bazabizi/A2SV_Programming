class Solution:
    def balancedString(self, s: str) -> int:
        length = (len(s))
        count = Counter(s)
        left = 0
        ans = float('inf')
        for right , letter in enumerate(s):
            count[letter] -= 1
            
            while max(count.values()) == length //4 and left < length:
                ans = min(ans,right - left + 1)
                count[s[left]] += 1
                left += 1
            

        
        return ans 
        