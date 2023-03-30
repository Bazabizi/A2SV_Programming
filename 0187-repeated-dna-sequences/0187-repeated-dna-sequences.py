class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        find = set()
        A = 0
        C = 0
        G = 0
        T = 0
        left = 0
        ans = set()
        for right, letter in enumerate(s):
            A <<= 1
            C <<= 1
            T <<= 1
            G <<= 1
            
            if letter == "A": A |= 1
            elif letter == "C": C |= 1
            elif letter == "T": T |= 1
            elif letter == "G":G |= 1
            
            if right - left + 1 == 10:
                if (A,C,T,G) in find:
                    ans.add(s[left:right + 1])
                find.add((A,C,T,G))
                
                
                if s[left] == "A": A ^= 1 << 9
                elif s[left] == "C": C ^= 1 << 9
                elif s[left] == "T": T ^= 1 << 9
                elif s[left] == "G": G ^= 1 << 9
                left += 1
            
#         ans = []
#         for val in count:
#             temp = ""
#             move = 512
#             for _ in range(10):
#                 if val[0] & move: temp += "A"
#                 elif val[1] & move: temp += "C"
#                 elif val[2] & move: temp += "T"
#                 elif val[3] & move: temp += "G"
#                 move >>= 1
#             ans.append(temp)
        
        return list(ans)