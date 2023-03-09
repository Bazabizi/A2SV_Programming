class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        bucket = [0] *k
        self.minimum = float('inf')
        cookies.sort(reverse = True)
        def distributer(i,bucket):
            if i >= len(cookies):
                self.minimum = min(self.minimum , max(bucket))
                return
            if max(bucket) >= self.minimum:
                return 
            
            for j in range(k):
                bucket[j] += cookies[i]
                distributer(i + 1 , bucket)
                bucket[j] -= cookies[i]
        
        distributer(0,bucket)
        return self.minimum