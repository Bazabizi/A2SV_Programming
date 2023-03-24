class Solution:
    def net(self, arr):
        count = defaultdict(int)
        for start , end in arr:
            count[start] -= 1
            count[end] += 1
        return max(count.values()) == 0
    
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        self.ans = 0
        def backtrack(idx , subRequest):
            if idx >= len(requests):
                return
            
            subRequest.append(requests[idx])
            if self.net(subRequest):
                self.ans = max( self.ans, len(subRequest) )
            backtrack(idx + 1 , subRequest)
            subRequest.pop()
            backtrack(idx + 1 , subRequest)
        backtrack(0 , [])
        return self.ans