class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        ans=defaultdict(int)
        result=0
        for i in nums:
            ans[i]+=1
        
        print(ans)
        for key in ans:
            if ans[key]!= 1:
                combination=1
                for i in range(1,ans[key]+1):
                    combination =combination *i
                for i in range(1,ans[key]-1):
                    combination /=i
                combination /=2
                result =result+combination
            combination=0
            print(result)
            result=int(result)
        return result