class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1Count = defaultdict(int)
        window = defaultdict(int)
        left = 0
        ans = 0
        length = len(s2)
        length_Of_S1 = len(s1)
        
        for letter in s1:
            s1Count[letter] += 1
        
        for right in range(length):
            window[s2[right]] += 1
            
            if right - left == length_Of_S1:
                window[s2[left]] -= 1
                if window[s2[left]] == 0:
                    window.pop(s2[left])
                left += 1
            
            if window == s1Count:
                return True
        
        return False