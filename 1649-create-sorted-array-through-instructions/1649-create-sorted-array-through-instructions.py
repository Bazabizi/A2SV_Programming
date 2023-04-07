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
            if left[l][0] > right[r][0]:
                right[r][2] += size1- l
                right[r][1] += l
                temp.append(right[r])
                r += 1
            elif left[l][0] < right[r][0]:
                temp.append(left[l])
                l += 1
            else:
                idx = l
                val = left[l][0]
                while l < size1 and right[r][0] == left[l][0]:
                    temp.append(left[l])
                    l += 1
                while r < size2 and right[r][0] == val:
                    right[r][2] += size1- l
                    right[r][1] += idx
                    temp.append(right[r])
                    r += 1
                
                
                
        while l < size1:
            temp.append(left[l])
            l += 1
        
        while r < size2:
            right[r][1] += l
            temp.append(right[r])
            r += 1
    
        return temp
        
    def createSortedArray(self, instructions: List[int]) -> int:
        size = len(instructions)
        nums = []
        for idx in range(size):
            nums.append([instructions[idx] , 0 , 0 ])
        ans = 0
        self.mergeSort(nums, 0 , len(instructions) - 1)
        
        for val , minVal , maxVal in nums:
            ans += min(minVal , maxVal)
        
        return ans % (10**9 + 7)
    