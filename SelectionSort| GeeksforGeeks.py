
class Solution: 
    def select(self, arr, i):
        # code here
        return arr
    
    def selectionSort(self, arr,n):
        #code here
        size = len(arr)
        for idx in range(size):
            minVal = idx
            for idx2 in range(idx+1,size):
                if arr[idx2]< arr[minVal]:
                    minVal = idx2
            arr[idx],arr[minVal] = arr[minVal],arr[idx]
