class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        bucket = [0] *k
        self.minimum = float('inf')
        cookies.sort(reverse = True)
        def backtrack(i,bucket):
            if i >= len(cookies):
                self.minimum = min(self.minimum , max(bucket))
                return
            if max(bucket) >= self.minimum:
                return 
            
            for j in range(k):
                bucket[j] += cookies[i]
                backtrack(i + 1 , bucket)
                bucket[j] -= cookies[i]
        
        backtrack(0,bucket)
        return self.minimum