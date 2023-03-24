class Solution:
    def mergeSort(self,nums , left, right ):
        if left == right:
            return [nums[left]]
        mid = left + (right - left) // 2
        leftnum = self.mergeSort(nums , left , mid  )
        rightnum = self.mergeSort(nums, mid + 1  , right)
        
        return self.merge(leftnum , rightnum)
    
    
    def merge(self,left , right):
        temp = []
        l = 0
        r = 0
        size1 = len(left)
        size2 = len(right)
        while l < size1 and r< size2:
            if left[l] > 2 * right[r]:
                self.ans += size1 - l
                r += 1
            else:
                l += 1
        l = 0
        r = 0
        while l < size1 and r< size2:
            if left[l] > right[r]:
                temp.append(right[r])
                r += 1
            else:
                temp.append(left[l])
                l += 1
        
        while l < size1:
            temp.append(left[l])
            l += 1
            
        while r < size2:
            temp.append(right[r])
            r += 1
        return temp
    
    def reversePairs(self, nums: List[int]) -> int:
        self.ans = 0
        self.mergeSort(nums, 0 , len(nums) - 1 )
        return self.ans