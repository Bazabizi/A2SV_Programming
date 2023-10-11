class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        ans = 0
        # print(nums)
        def search(arr ,idx ,  num):
            left = idx - 1
            right = len(arr)
            
            while left + 1 < right:
                mid = left + (right - left)//2
                if arr[mid] > num:
                    right = mid
                else:
                    left = mid
            return right
            
            
        for i , num in enumerate(nums):
            val = target - nums[i]
            if val < 0:
                continue
            
            index = search(nums , i , val)
            
            if index == i:
                if 2*nums[i] > target:
                    continue
            if index == len(nums) or nums[index] > val:
                index -= 1
            # print(i ,index)
            size = index - i
            ans += 2**(size)
            # print(ans)
            
        
        return (ans)%(10**9 + 7)