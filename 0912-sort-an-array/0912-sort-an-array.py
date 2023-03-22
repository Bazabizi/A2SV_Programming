class Solution:
    def merge(self,leftArray,rightArray):
        temp = []
        l= len(leftArray)
        r = len(rightArray)
        left = 0
        right = 0 
        while left < l and right < r:
            if leftArray[left] >= rightArray[right]:
                temp.append(rightArray[right])
                right += 1
            else:
                temp.append(leftArray[left])
                left += 1
        
        while left < l:
            temp.append(leftArray[left])
            left += 1

        while right < r:
            temp.append(rightArray[right])
            right += 1
            
        return temp
        
    def mergeSort(self,left, right, arr):
        if left == right:
            return [arr[left]]
        mid = (right + left ) // 2
        
        leftArray = self.mergeSort(left , mid , arr)
        rightArray = self.mergeSort(mid + 1 , right, arr)
        return self.merge(leftArray , rightArray)
        
    def sortArray(self, nums: List[int]) -> List[int]:
        
        return self.mergeSort(0, len(nums)-1 , nums)