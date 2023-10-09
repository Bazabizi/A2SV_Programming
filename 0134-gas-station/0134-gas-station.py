class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        difference = []
        ans = -1
        for g , c in zip(gas , cost):
            difference.append(g - c)
        if sum(difference) < 0:
            return -1
        
        total = 0
        for idx , num in enumerate(difference):
            total += num
            # print(total)
            if total < 0:
                ans = - 1
                total = -1
            if total >= 0 and ans == -1:
                ans = idx
        
        return ans