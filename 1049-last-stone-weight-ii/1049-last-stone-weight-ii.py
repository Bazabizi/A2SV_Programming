class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        mem = defaultdict(int)
        def dp(total , idx,inserted):
            if idx >= len(stones):
                if inserted != idx:
                    return abs(total*2 - sum(stones))
                else:
                    return stones[-1]
            if (idx, total) in mem:
                return mem[(idx , total)]
            
            mem[(idx , total)] = min(dp(total + stones[idx] , idx + 1 , inserted + 1) ,
                                     dp(total , idx + 1 , inserted))
            return mem[(idx , total)] 
        
        
        return dp( 0, 0 ,0)