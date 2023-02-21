class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        size = n
        index = 0
        array =[i for i in range(1, n+1)]
        if k > n:
            k = k % n
        while size > 1:
            count = k
            while count > 1:
                index += 1
                if index ==n:
                    index = 0
                if array[index]!=0:
                    count -= 1
                
            array[index] = 0
            while array[index]==0:
                index +=1
                if index ==n:
                    index = 0 
            size -= 1
        for num in array:
            if num!= 0:
                return num
                