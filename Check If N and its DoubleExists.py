class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        size=len(arr)

        for idx in range(size):
            val=arr[idx]*2
            if val in arr and arr.index(val)!=idx:
                return True
                
        return False
