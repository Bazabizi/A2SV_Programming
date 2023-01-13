class Solution:
    def convert(self, s: str, numRows: int) -> str:
        size= len(s)
        temp =[["0" for _ in range(size)]for _ in range(numRows)]
        col = 0
        length = 0
        row = 0
        if numRows == 1:
            return s
        
        while length < size:
            while row < numRows and length< size:
                temp[row][col] = s[length]
                length +=1
                row +=1
            row -=2
            col +=1
            
            while row >=0 and col < size and length < size:
                temp[row][col] = s[length]
                row -= 1
                col += 1
                length +=1
            row = 1
            col -=1
        ans=""
        
        for rows in range(numRows):
            for cols in range(size):
                if temp[rows][cols] != '0':
                    ans += str(temp[rows][cols])
        
        return ans
            