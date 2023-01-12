class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        rowSize= len(strs)
        colSize =len(strs[0])
        ans = 0
        for col in range(colSize):
            temp = strs[0][col]
            check = True
            
            for row in range(1, rowSize):
                if ord(temp) <= ord(strs[row][col]):
                    temp = strs[row][col]
                else:
                    check = False
                    break
            if not check :
                ans +=1
                
        return ans