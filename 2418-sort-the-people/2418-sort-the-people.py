class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        size = len(heights)
        
        for idx in range(size):
            for idx2 in range(size-1,idx,-1):
                if heights[idx2] > heights[idx2-1]:
                    heights[idx2] , heights[idx2-1] = heights[idx2-1] , heights[idx2]
                    names[idx2] , names[idx2-1] = names[idx2-1] , names[idx2]

        return names
        
        
                