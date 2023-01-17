class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        size = len(heights)
        temp=heights.copy()
        for idx in range(size):
            for idx2 in range(size-1,idx,-1):
                if heights[idx2] > heights[idx2-1]:
                    heights[idx2] , heights[idx2-1] = heights[idx2-1] , heights[idx2]
        ans = []
        
        for num in heights:
            man = temp.index(num)
            ans.append(names[man])
        return ans
        
        
                