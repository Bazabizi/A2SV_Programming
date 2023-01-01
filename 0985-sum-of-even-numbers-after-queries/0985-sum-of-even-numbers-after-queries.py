class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        sum=0
        for num in nums:
            if num %2==0:
                sum += num
        ans=[]
        
        for num in queries:
            if num[0] %2 and nums[ num[1] ] %2 :
                sum += num[0] +nums[ num[1] ]
            
            elif num[0] %2 and nums[ num[1] ] %2==0:
                sum -= nums[num[1]]
                
            elif num[0] %2 == 0 and nums[ num[1] ] %2 == 0:
                sum += num[0]
            nums[num[1]] += num[0]
            ans.append(sum)
        
        return ans