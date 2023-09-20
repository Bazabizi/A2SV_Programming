class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        length = len(nums)
        arr = [1]*length
        counter = [1]*length
        
        for idx in range(length):
            for idx2 in range(idx - 1 , -1 , -1):
                if nums[idx] > nums[idx2]:
                    if arr[idx2] >= arr[idx]:
                        arr[idx] = arr[idx2] + 1
                        counter[idx] = 0
                    if arr[idx2] + 1 == arr[idx]:
                        counter[idx] += counter[idx2]
        max_length = max(arr)
        ans = 0
        
        for idx , num in enumerate(arr):
            if num == max_length:
                ans += counter[idx]
        
        return ans