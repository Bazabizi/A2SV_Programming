class Solution:
    def subarrayGCD(self, nums: List[int], k: int) -> int:
        ans = 0
        for idx , num in enumerate(nums):
            if num < k or num%k != 0:
                continue
            gcd = num
            for val in nums[idx:]:
                gcd = math.gcd(gcd , val)
                if gcd < k:
                    break
                if gcd == k:
                    ans += 1
        return ans
                