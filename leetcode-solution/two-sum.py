class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prefix = defaultdict(int)
        for idx , num in enumerate(nums):
            val = target - num
            if val in prefix:
                return [prefix[val] , idx]
            prefix[num] = idx
        