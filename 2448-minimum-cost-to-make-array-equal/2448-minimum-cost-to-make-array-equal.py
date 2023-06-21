class Solution:
    def minCost(self, nums: List[int], cost: List[int]) -> int:
        def total_cost(val):
            total  = 0
            for num , c in zip(nums , cost):
                total += abs(num - val)*c
            
            return total
        
        left = min(nums) - 1
        right = max(nums) + 1
        while left + 1 < right:
            mid = left + (right - left)//2
            cost_1 = total_cost(mid)
            cost_2 = total_cost(mid + 1)
            
            if cost_1 > cost_2:
                left = mid
            else:
                right = mid
            
        return total_cost(right)