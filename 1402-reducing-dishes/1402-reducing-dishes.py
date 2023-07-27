class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        ans = 0
        satisfaction.sort(reverse = True)
        total = 0
        maxval = 0
        for num in satisfaction:
            total += num
            if total < 0:
                break
            ans += total
        
        return ans