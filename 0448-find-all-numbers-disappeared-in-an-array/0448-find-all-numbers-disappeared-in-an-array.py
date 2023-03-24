class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        size = len(nums)
        idx = 0
        ans = []
        while idx < size:
            if nums[idx] != idx + 1:
                
                if nums[ nums[idx] - 1 ] == nums[idx]:
                    idx += 1  
                else:
                    idx2 = nums[idx] - 1
                    nums[idx] , nums[idx2] = nums[idx2] , nums[idx] 
                    
            else:
                idx += 1
        
        for num in range(1, size + 1):
            if num != nums[num - 1]:
                ans.append(num)
        return ans