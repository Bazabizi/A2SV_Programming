class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        size = len(arr)
        stack = []
        ans = 0
        for idx , val in enumerate(arr):
            
            while stack and stack[-1][0] >= val:
                cur  = stack[-1][0]
                curIdx = stack[-1][1]
                
                right= (idx - curIdx)
                stack.pop()
                if stack:
                    left = (curIdx - stack[-1][1] )
                else:
                    left = curIdx + 1
                
                ans += (right*left)* cur
                
                
            stack.append((val,idx))
            
        while stack:
            cur  = stack[-1][0]
            curIdx = stack[-1][1]
            right= (size - curIdx)
            stack.pop()
            if stack:
                left = (curIdx - stack[-1][1] )
            else:
                left = curIdx + 1
                
            ans += (right*left)*cur     
                
                
        return ans%(10**9 +7)