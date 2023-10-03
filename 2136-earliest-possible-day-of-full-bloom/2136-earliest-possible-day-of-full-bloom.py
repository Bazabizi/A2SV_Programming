class Solution:
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:
        ans = 0
        newArr = []
        for grow , plant in zip(growTime , plantTime):
            newArr.append([grow , plant])
        
        newArr.sort(reverse = True)
        
        
        init = 0
        for grow , time in newArr:
            init += time
            ans = max(ans , init + grow + 1)
            
        return ans - 1