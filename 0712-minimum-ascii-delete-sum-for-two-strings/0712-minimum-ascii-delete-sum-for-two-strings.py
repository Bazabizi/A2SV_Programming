class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        mem = defaultdict(int)
        
        def dp(idx1 , idx2):
            
            if (idx1 , idx2) in mem:
                return mem[(idx1 , idx2)]
            
            if idx1 < 0:
                val = 0
                for letter in s2[:idx2+1 ]:
                    val += ord(letter)
                
                return val
            
            if idx2 < 0:
                val = 0
                for letter in s1[:idx1+1]:
                    val += ord(letter)
                
                return val
            
            
            
            if s1[idx1] == s2[idx2]:
                mem[(idx1 , idx2)] = dp( idx1 - 1 , idx2 - 1)
            else:
                
                mem[(idx1 , idx2)] = min(ord(s1[idx1]) + dp(idx1 -1 , idx2) ,
                                         ord(s2[idx2]) + dp(idx1 , idx2 - 1)
                                        )
                             
            return mem[(idx1 , idx2)]
        
        return dp(len(s1) - 1 , len(s2) - 1)