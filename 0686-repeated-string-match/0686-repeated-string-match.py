class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        def kmp(p : str) -> list:
            m = len(p)
            prevLPS, i = 0, 1
            LPS = [0 for _ in range(m)]
            while i < m:
                if p[prevLPS] == p[i]:
                    LPS[i] = prevLPS + 1
                    prevLPS += 1
                    i += 1
                else:
                    if prevLPS == 0:
                        i += 1
                    else:
                        prevLPS = LPS[prevLPS - 1]
            return LPS
    
        lps = kmp(b)
        i = 0
        x = max(len(a) , len(b))
        y = min(len(a), len(b))
        for k in range(1,4*x//y):
            j = 0
            while j < len(a):
                
                if a[j] != b[i]:
                    if i == 0:
                        j += 1
            
                    else:
                        i = lps[i-1]
                else:
                    i += 1
                    j += 1
                if i == len(b):
                    return k
            if i == len(b):
                    return k
        return -1
        
        
        