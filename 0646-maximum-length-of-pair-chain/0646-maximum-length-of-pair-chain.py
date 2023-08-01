class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        length = len(pairs)
        pairs.sort()
        ans = [0]*length
        
        ans[-1] = 1
        
        if length > 1:
            if pairs[-1][0] > pairs[-2][1]:
                ans[-2] = 2
                
        for idx in range(length - 3 , -1 , -1):
            find = False
            for index in range(idx + 1 , length):
                if pairs[index][0] > pairs[idx][1]:
                    find = True
                    ans[idx] = max(ans[idx] , ans[index])
            if find:
                ans[idx] += 1
                
        return max(ans)
        