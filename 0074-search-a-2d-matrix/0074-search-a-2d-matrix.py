class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        right = len(matrix)-1
        left = 0
        middle = (left + right)//2
        notFound = True
        while left <= right:
            if target >= matrix[middle][0]:
                if target <= matrix[middle][-1]:
                    row = middle
                    notFound = False
                    break
                else:
                    left = middle + 1
            else:
                right = middle - 1
            middle = (left + right)//2
        
        if notFound :
            return False
        
        right = len(matrix[row])-1
        left = 0
        middle = (left + right)//2
        
        while left <= right:
            if matrix[row][middle] == target:
                return True 
            elif matrix[row][middle] > target:
                right = middle -1
            else:
                left = middle + 1
            
            middle = (left + right)//2
        
        return False
            
            
        
        
        