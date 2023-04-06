class Solution:
    def quickSort(self,arr):
        if len(arr) <= 1:
            return arr
        pivot = arr[0]
        left = []
        right = []
        for num in arr[1:]:
            if num[0] <= pivot[0]:
                left.append(num)
            else:
                right.append(num)
        return self.quickSort(left) + [pivot] + self.quickSort(right)
    
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count =Counter(nums)
        arr = []
        for num in count.keys():
            arr.append([count[num] , num])
        
        arr = self.quickSort(arr)
        size = len(arr)
        idx = size - k
        ans = []
        
        while idx < size:
            ans.append(arr[idx][1])
            idx += 1
            
        return ans