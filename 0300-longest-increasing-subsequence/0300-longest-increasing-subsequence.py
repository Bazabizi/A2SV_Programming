class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        length = len(nums)
        arr = [1]*length
        for idx in range(length):
            count = 1
            for idx2 in range(idx - 1 , -1 , -1):
                if nums[idx2] < nums[idx]:
                    count = max(count , arr[idx2] + 1)
            
            arr[idx] = count
        
        return max(arr)