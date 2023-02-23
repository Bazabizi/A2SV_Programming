class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        countFruit = defaultdict(int)
        ans = 0
        left = 0
        length = len(fruits)
        for right in range(length):
            countFruit[ fruits[right] ] += 1
                
            if len(countFruit) > 2:
                
                while min(countFruit.values())!= 0 and left < length:
                        
                    countFruit[ fruits[left] ] -= 1
                    left += 1
                if left > 0 and countFruit[ fruits[left-1] ] == 0:
                        countFruit.pop(fruits[left-1])
                     
            window = right - left + 1 
            ans = max(ans, window)
        
        return ans