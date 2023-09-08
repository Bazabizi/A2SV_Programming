class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
     
        ans = [[1]]
        for i in range(1 , numRows):
            temp = [0]*(i + 1)
            for j in range(i+1):
                if j != 0:
                    temp[j] += ans[i - 1][j-1]
                if j != i:
                    
                    temp[j] += ans[i- 1][j]
            ans.append(temp)
        
        return ans