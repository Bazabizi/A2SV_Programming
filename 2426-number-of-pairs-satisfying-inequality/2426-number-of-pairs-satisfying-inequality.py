class Solution:
    def mergeSort(self,num , left , right):
        if left == right:
            return [num[left]]
        mid = (left + right) // 2 
        lefthalf = self.mergeSort(num , left , mid )
        righthalf = self.mergeSort(num , mid + 1 , right)
        return self.merge(lefthalf, righthalf)
    
    def merge(self,left , right):
        size1 = len(left)
        size2 = len(right)
        l = 0
        r = 0
        while l < size1 and r < size2:
           
            if left[l][0] - left[l][1] <= self.diff  + right[r][0] - right[r][1]:
                self.ans += size2 - r
                l += 1
            else:
                r += 1
        temp = []
        l = 0
        r = 0
        while l < size1 and r < size2:
            
            if left[l][0] - left[l][1] <=  right[r][0] - right[r][1] :
                temp.append(left[l])
                l += 1
            else:
                temp.append(right[r])
                r += 1
        
        while l < size1:
            temp.append(left[l])
            l += 1
            
        while r < size2:
            temp.append(right[r])
            r += 1
            
        return temp
    
    
    def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:
        self.diff = diff
        self.ans = 0
        num = list(zip(nums1 , nums2))
        self.mergeSort(num , 0 , len(num) - 1)
        return self.ans