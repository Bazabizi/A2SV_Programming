class Solution:
    def isPrime(self, num):
        n = 2
        while n*n <= num:
            if num % n == 0:
                return False
            n += 1
        return True
    
    def closestPrimes(self, left: int, right: int) -> List[int]:
        temp = []
        ans = [-1, -1]
        
        for num in range(left,right + 1):
            if num != 1 and self.isPrime(num):
                temp.append(num)
            if len(temp)>= 2 and temp[-1] -  temp[-2] <=2:
                return temp[-2] , temp[-1]
        size = len(temp)
        
        if size >1:
            ans[0] = temp[0]
            ans[1] = temp[1]
        for idx in range(size - 1):
            if ans[1] - ans[0] <= 2:
                break
            if ans[1] - ans[0] > temp[idx + 1] - temp[idx]:
                ans[1] = temp[idx + 1]
                ans[0] = temp[idx]
            
        return ans