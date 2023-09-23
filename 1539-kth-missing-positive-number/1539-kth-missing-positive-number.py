class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        left, right = 0, len(arr)
        
        while left + 1 < right:
            mid = (left + right) // 2
            missing = arr[mid] - (mid + 1)
            
            if missing < k:
                left = mid 
            else:
                right = mid
        if left == 0 and k < arr[0]:
            return k
            
        return arr[left] + k - arr[left ] + left + 1