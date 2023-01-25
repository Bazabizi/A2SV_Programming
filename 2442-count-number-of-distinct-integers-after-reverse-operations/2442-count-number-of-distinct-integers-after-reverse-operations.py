class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        ans = set(nums)
        for num in nums:
            
            temp = 0
            while num >0:
                x = num%10
                temp =temp*10 +x 
                
                num //=10
            ans.add(temp)
            
        return len(ans)
                