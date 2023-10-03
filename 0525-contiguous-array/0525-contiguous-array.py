class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        prefix = defaultdict(int)
        prefix[0] = -1
        ans = 0
        sum_ = 0

        for idx, val in enumerate(nums):
            if val == 0:
                sum_ -= 1
            elif val == 1:
                sum_ += 1

            if sum_ in prefix:
                ans = max(ans, idx-prefix[sum_])
            else:
                prefix[sum_] = idx
                
        return ans