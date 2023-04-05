class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
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