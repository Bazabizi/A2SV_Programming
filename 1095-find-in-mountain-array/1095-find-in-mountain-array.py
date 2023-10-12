# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        left = 0
        size = mountain_arr.length()
        right = size
        while left + 1 < right:
            
            mid = left + (right - left)//2
            val = mountain_arr.get(mid)
            # print(mid)
            l = mountain_arr.get(mid - 1)
            r = mountain_arr.get(mid + 1)
            if  l <= val <= r:
                left = mid
            elif l >= val >= r:
                right = mid
            else:
                right = mid
                break
        center = right
        # print(right)
        left = -1
        while left + 1 < right:
            mid = left + (right - left)//2
            val = mountain_arr.get(mid)
            if val >= target:
                right = mid
            else:
                left = mid
        
        if right < size and  mountain_arr.get(right) == target:
            return right
        
        left = center
        right = size
        
        while left + 1 < right:
            mid = left + (right - left)//2
            val = mountain_arr.get(mid)
            if val <= target:
                right = mid
            else:
                left = mid
        
        if right < size and mountain_arr.get(right) == target:
            return right
        return  -1