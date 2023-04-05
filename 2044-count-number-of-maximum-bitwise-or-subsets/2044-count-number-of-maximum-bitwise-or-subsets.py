class Solution:
    def Subset(self,nums):
        subset = []
        num = 1<<len(nums)
        
        for n in range(num):
            sub = []
            val = 1
            idx = 0
            while val <= n:
                if n & val:
                    sub.append(nums[idx])
                idx += 1
                val <<= 1
            subset.append(sub)
        return subset
    
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        maxVal = 0
        subset = self.Subset(nums)
        for num in nums:
            maxVal |= num
        
        ans = 0
        for arr in subset:
            temp = 0
            for val in arr:
                temp |= val
                if temp == maxVal:
                    ans += 1
                    break
        
        return ans