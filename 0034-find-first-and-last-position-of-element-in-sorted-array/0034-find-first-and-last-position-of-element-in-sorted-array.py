class Solution:
    def leftBisect(self,arr,left,right, target):
        if right != 0 and arr[right - 1 ] < target:
            return right
        else:
            while left <= right:
                mid = (left + right) // 2
                if arr[mid] < target and arr[mid + 1] == target:
                    return mid + 1
                elif arr[mid] == target and mid != 0 and arr[mid - 1 ] == target:
                    right = mid - 1
                
                elif arr[mid] < target:
                    left = mid + 1
                elif arr[mid ] == target and (mid == 0 or arr[mid-1] < target):
                    return mid
                else:
                    right = mid - 1 
        return right
    def rightBisect(self,arr, left,right, target):
        if left != len(arr) -1  and arr[left + 1 ] > target:
            return left
        else:
            while left <= right:
                mid = (left + right) // 2
                if arr[mid] > target and arr[mid - 1] == target:
                    return mid - 1
                elif arr[mid] == target and mid != len(arr)-1 and arr[mid + 1 ] == target:
                    left = mid + 1
                
                elif arr[mid] > target:
                    right = mid - 1
                elif arr[mid ] == target and (mid == len(arr) - 1 or arr[mid + 1] > target):
                    return mid
                else:
                    left = mid + 1 
        return left
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = 0
        right = len(nums) - 1
        leftFound = -1
        rightFound = -1
        
        while left <= right:
            mid = (left + right ) // 2
            if nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target :
                
                left = mid + 1
            
            else:
                leftFound = self.leftBisect(nums,left,mid, target)
                rightFound = self.rightBisect(nums,mid,right,target)
                break
                
        return leftFound, rightFound