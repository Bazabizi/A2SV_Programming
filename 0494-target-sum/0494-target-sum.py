class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        mem = defaultdict(int)
        def calTarget(sums, idx):
            if idx >= len(nums):
                if sums == target:
                    return 1
                else:
                    return 0

            if (sums, idx) in mem:
                return mem[(sums, idx)]

            left = calTarget(sums - nums[idx], idx+1)
            right = calTarget(sums + nums[idx], idx + 1)

            mem[(sums, idx)]  = left + right
            return mem[(sums, idx)]

        return calTarget(0, 0)