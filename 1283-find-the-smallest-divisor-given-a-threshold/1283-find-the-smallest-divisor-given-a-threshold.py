class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        def Sums(divisor):
            total = 0
            for num in nums:
                total += ceil(num/divisor)
            
            return total <= threshold
        
        
        left = 0
        right = max(nums) + 1
        
        while left + 1 < right :
            mid = left + (right - left) // 2
            
            if Sums(mid):
                right = mid
            else:
                left = mid
        
        return right