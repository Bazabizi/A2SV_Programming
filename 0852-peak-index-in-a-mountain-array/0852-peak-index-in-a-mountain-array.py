class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        left = 0 
        right = len(arr) - 1
        
        while left + 1 < right:
            mid = (left + right) //2
            
            if arr[mid] >= arr[right]:
                right -= 1
            else:
                left = mid
            
        
        return right