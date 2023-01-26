class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        squareList = []
        ans = False
        
        for num in range(c+1):
            if num**2 <=c:
                squareList.append(num**2)
            else:
                break
        left = 0
        right = len(squareList) -1
        
        while left <= right:
            total = squareList[left] +squareList[right]
            if total < c:
                left +=1
            elif total > c:
                right -=1
            else:
                ans = True
                break
            
        return ans
        