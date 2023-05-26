class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        arr.sort()
        length = len(arr)
        arr[0] = 1
        for idx in range(1 , len(arr)):
            if abs(arr[idx] - arr[idx - 1]) > 1:
                arr[idx] = arr[idx- 1] + 1
        
        return arr[-1]