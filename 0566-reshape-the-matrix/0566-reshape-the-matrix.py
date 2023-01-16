class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        if r*c != len(mat)* len(mat[0]):
            return mat
        ans = [[0 for _ in range(c)] for _ in range(r)]
        temp=[]
        rowSize= len(mat)
        colSize = len(mat[0])
        
        for row in range(rowSize):
            for col in range(colSize):
                temp.append(mat[row][col])
        idx=0
        for row in range(r):
            for col in range(c):
                ans[row][col]= temp[idx]
                idx += 1
        
        return ans