class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        change = defaultdict(int)
        for val in bills:
            if val == 10:
                if change[5] < 1:
                    return False
                change[5] -= 1
            
            elif val == 20:
                if change[10] >= 1 and change[5] >= 1:
                    change[10] -= 1
                    change[5] -= 1
                elif change[5] >= 3:
                    change[5] -= 3
                else:
                    return False
            
            change[val] += 1
        
        return True