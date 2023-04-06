class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans = 0
        check = False
        for val in range(31,-1,-1):
            count = 0
            negative = 0
            for num in nums:
                if num < 0:
                    negative += 1
                    num = ~num
                if num & (1<<val):
                    count += 1
            if count % 3:
                ans += 1<<val
            if negative %3 :
                check = True
        if check:
            return ~ans
        return ans