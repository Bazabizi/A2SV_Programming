class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        check = False
        size = len(arr)
        index = 0
        for idx in range(size-1):
            if arr[idx] < arr[idx+1]:
                check = True
            if arr[idx] >= arr[idx+1]:
                index = idx
                break
            
        if check:
            for idx in range(index,size-1):
                if arr[idx]<=arr[idx+1]:
                    return False
        return check
        
            