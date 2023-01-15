class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        rowSize = len(matrix)
        colSize = len(matrix[0])
        size = colSize*rowSize
        count = 0
        right = colSize-1
        left = 0
        top = 0
        bottom = rowSize
        ans =[]
        while count < size:
            # to the right
            for col in range(left, right+1):
                ans.append(matrix[left][col])
                count +=1
            left +=1
            
            if count >= size:
                break
                
            # to the bottom
            for row in range(top+1,bottom):
                ans.append(matrix[row][right])
                count +=1
            top += 1
            if count >= size:
                break
                
            #to the left
            for col in range(right-1,left-2,-1):
                ans.append(matrix[bottom-1][col])
                count +=1
            right -= 1
            
            if count >= size:
                break
                
            # to the top
            for row in range(bottom-2,top-1,-1):
                ans.append(matrix[row][left-1])
                count +=1
            bottom -= 1
            
        
        return ans
            
            
                    
        