class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        ans=defaultdict(int)
        pair=0
        
        for num in nums:
            pair += ans[num]
            ans[num]+=1
        return pair