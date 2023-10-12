class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        prefix = [0]
        prefix.append(travel[0])
        for num in travel[1:]:
            val = prefix[-1]
            prefix.append(val+num)
        
        m,g,p = 0 , 0 , 0
        idxm , idxg , idxp= -1 , -1 , -1
        
        for idx , trash in enumerate(garbage):
            for l in trash:
                if l == "M":
                    m += 1
                    idxm = idx
                if l == "G":
                    g += 1
                    idxg = idx
                if l == "P":
                    p += 1
                    idxp = idx
        
        ans = 0
        if idxg != -1:
            ans += g + prefix[idxg]
        if idxp != -1:
            ans += p + prefix[idxp]
        if idxm != -1:
            ans += m + prefix[idxm]
        
        return ans