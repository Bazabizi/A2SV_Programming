class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        right = sum(nums) + 1
        left = max(nums) - 1
        
        
        def isValid(val):
            count = 0
            total = 0
            
            for num in nums:
                total += num
                if total == val:
                    count += 1
                    total = 0
                elif total > val:
                    count += 1
                    total = num
            if total == 0:
                return count
            return count + 1
        
        while left + 1 < right:
            mid = left + (right - left)//2
            
            if isValid(mid) <= k:
                right = mid
            else:
                left = mid
        
        return right 
        