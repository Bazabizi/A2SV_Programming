class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        winAll=[]
        lossOne=[]
        result=[]
        winner=defaultdict(int)
        losser=defaultdict(int)
        for num in matches:
            winner[num[0]]+=1
        for num in matches:
            losser[num[1]]+=1
        
        for key in winner:
            if losser[key]==0:
                winAll.append(key)
                
        for key in losser:
            if losser[key]==1:
                lossOne.append(key)
        
        winAll.sort()
        lossOne.sort()
        
        result.append(winAll)
        result.append(lossOne)
        return result