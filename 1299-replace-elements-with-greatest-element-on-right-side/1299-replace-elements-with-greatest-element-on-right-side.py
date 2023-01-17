class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        maxVal=arr[-1]
        size = len(arr)
        for idx in range(size-2,-1,-1):
            temp= arr[idx]
            arr[idx] = maxVal
            if temp > maxVal:
                maxVal = temp
        arr[-1] = -1
        return arr