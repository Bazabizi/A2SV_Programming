class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        size = len(nums)
        ans = set()
        idx = 0
        while idx < size:
            if nums[idx] != idx + 1:
                
                if nums[ nums[idx] - 1 ] == nums[idx]:
                    ans.add(nums[idx])
                    idx += 1
                else:
                    idx2 = nums[idx] - 1
                    nums[idx] , nums[idx2] = nums[idx2] , nums[idx] 
                    
            else:
                idx += 1
        
        return list(ans)
   
    
    
    
    
    