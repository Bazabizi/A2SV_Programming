class Solution:
    def similarPairs(self, words: List[str]) -> int:
        size=len(words)
        pair=0
        
        for idx1 in range(size):
            for idx2 in range(idx1+1,size):
                if Counter(words[idx1]).keys()== Counter(words[idx2]).keys():
                    pair+=1
        
        return pair