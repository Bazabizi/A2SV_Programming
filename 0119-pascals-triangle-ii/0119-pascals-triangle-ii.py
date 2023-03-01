class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        else:
            newArray = [1]*(rowIndex + 1)
            if rowIndex > 1:
                left = 0
                right = 1
                array = self.getRow(rowIndex - 1)
                while right < rowIndex:
                    newArray[right] = array[left] + array[right]
                    right += 1
                    left += 1
    
            return newArray