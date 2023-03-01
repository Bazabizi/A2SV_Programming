class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
       
        newArray = [1]*(rowIndex + 1)
        
        if rowIndex > 1:
            array = self.getRow(rowIndex - 1)
            for index in range(1,rowIndex):
                newArray[index] = array[index - 1] + array[index]
    
        return newArray