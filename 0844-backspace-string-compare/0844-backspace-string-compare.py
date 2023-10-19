class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        newS = []
        newT = []
        for l in s:
            if l == "#":
                if newS:
                    newS.pop()
                continue
            newS.append(l)
        for l in t:
            if l == "#":
                if newT:
                    newT.pop()
                continue
            newT.append(l)
        
        return "".join(newS) == "".join(newT)