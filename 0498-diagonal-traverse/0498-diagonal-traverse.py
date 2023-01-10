class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        m= len(mat[0])
        n= len(mat)
        row = 0
        col = 0
        ans =[]
        count = 1
        temp=[]
        while row < n :
            col=0
            temp1=row
            if count%2==0:
                while row>=0 and col< m:
                    temp.append(mat[row][col])
                    row -=1
                    col +=1
                size = len(temp)
                
                for idx in range (size-1,-1,-1):
                    ans.append(temp[idx])
                temp=[]
            else:
                while row >= 0 and col < m:
                    ans.append(mat[row][col])
                    row-=1
                    col+=1
            count += 1
            row = temp1 + 1
        
        col = 1
        while col < m :
            row=n-1
            temp1 = col
            if count%2==0:
                while col<m and row>=0:
                    temp.append( mat[row][col])
                    row -=1
                    col +=1
                size = len(temp)
                
                for idx in range (size-1,-1,-1):
                    ans.append(temp[idx])
                temp=[]
            else:
                while col < m and row>=0:
                    ans.append(mat[row][col])
                    row-=1
                    col+=1
            count += 1
            col = temp1 + 1
            
        return ans
            