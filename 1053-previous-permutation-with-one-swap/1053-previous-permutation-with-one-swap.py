class Solution:
    def prevPermOpt1(self, arr: List[int]) -> List[int]:
        size = len(arr)
        for idx in range(size - 2 , -1 , -1):
            if arr[idx] > arr[idx + 1]:
                index = idx
                maxval = float('-inf')
                for i in range(idx , size):
                    if maxval < arr[i] and arr[i] < arr[idx]:
                        index = i
                        maxval = arr[i]
                else:
                    arr[idx] , arr[index] = arr[index] , arr[idx]
                    break
        
        return arr