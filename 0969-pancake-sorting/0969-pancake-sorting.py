class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        ans = []
        size  = len(arr)
        for idx in range(size,0,-1):
            index = arr.index(idx)
            if arr.index(idx) != idx-1:
                ans.append(index+1)
                arr[:index+1] = arr[:index+1][::-1]
                ans.append(idx)
                arr[:idx] = arr[:idx][::-1]
       
        return ans
            