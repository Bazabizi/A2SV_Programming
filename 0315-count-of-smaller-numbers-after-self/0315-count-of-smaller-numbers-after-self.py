class Solution:
    def mergeSort(self,arr, left,right):
        if left == right:
            return [arr[left]]
        
        mid = (left + right) // 2
        left_half = self.mergeSort(arr,left ,mid)
        right_half = self.mergeSort(arr , mid + 1 , right)
        
        return self.merge( left_half , right_half )
    
    
    def merge(self, left ,right):
        size1 = len(left)
        size2 = len(right)
        l = 0
        r = 0
      
        temp = []
        while l < size1 and r < size2:
            if left[l][0] <= right[r][0]:
                self.ans[left[l][1]] += r
                temp.append(left[l])
                l += 1
            else:
                temp.append(right[r])
                r += 1
                    
        
        while l < size1:
            self.ans[left[l][1]] += size2
            temp.append(left[l])
            l += 1
            
        while r < size2:
            temp.append(right[r])
            r += 1
        
        return temp
    
    
    def countSmaller(self, nums: List[int]) -> List[int]:
        length = len(nums)
        self.ans = [0]*(length)
        num = []
        for idx in range(length):
            num.append([nums[idx] , idx ])
        
        self.mergeSort(num , 0 , length - 1)
        
        return self.ans