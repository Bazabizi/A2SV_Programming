class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        arr = [0]*102
        for birth , death in logs:
            arr[birth - 1950] += 1
            arr[death - 1950 ] -= 1

        for i in range(1 , 102):
            arr[i] += arr[i-1]

        maxpop = max(arr)
        for i , num in enumerate(arr):
            if num == maxpop: 
                return i + 1950
        
        return 1950