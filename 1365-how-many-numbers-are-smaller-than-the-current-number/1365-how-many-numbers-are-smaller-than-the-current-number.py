class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        ans =  nums.copy() 
        nums.sort()
        position = defaultdict(int)
        length = len(nums)
        
        for idx in range(length):
            if nums[idx] not in position:
                position[nums[idx]] = idx
                
        for idx in range(length):
            ans[idx] = position[ans[idx]]
        return ans