class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        size = len(heights)
        
        #bubble sort
        # for idx in range(size):
        #     for idx2 in range(size-1,idx,-1):
        #         if heights[idx2] > heights[idx2-1]:
        #             heights[idx2] , heights[idx2-1] = heights[idx2-1] , heights[idx2]
        #             names[idx2] , names[idx2-1] = names[idx2-1] , names[idx2]

        #selection sort
        
        for idx in range(size):
            minidx= idx
            for idx2 in range(idx+1,size):
                if heights[idx2] > heights[minidx]:
                    minidx = idx2
            
            heights[idx] ,heights[minidx] =heights[minidx] ,heights[idx] 
            names[idx] ,names[minidx] = names[minidx] ,names[idx] 
            
        return names
        
        
                