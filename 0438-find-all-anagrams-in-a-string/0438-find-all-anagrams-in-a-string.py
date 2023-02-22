class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        p_count = defaultdict(int)
        s_count = defaultdict(int)
        for letter in p:
            p_count[letter]+=1
        
        size = len(s)
        length = len(p)
        left = 0
        ans = []
        
        for right in range(size):
            s_count[s[right]] += 1
            
            if right - left == length:
                s_count[s[left]] -= 1
                if s_count[s[left]]==0:
                    s_count.pop(s[left])
                left +=1
            if s_count == p_count:
                ans.append(left)
                
        return ans