class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        count = defaultdict(int)
        left = 0
        ans1 = 0
        ans2 = 0
        for right , num in enumerate(nums):
            count[num] += 1
            while len(count) >k and left <=right:
                count[nums[left]] -= 1
                if count[nums[left]] == 0:
                    count.pop(nums[left])
                left += 1
            
            ans1 += right - left + 1
        left = 0
        count.clear()
        for right , num in enumerate(nums):
            count[num] += 1
            while len(count) > k - 1 and left <=right:
                count[nums[left]] -= 1
                if count[nums[left]] == 0:
                    count.pop(nums[left])
                left += 1
            
            ans2 += right - left + 1
        
        return ans1 - ans2