class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        self.combinations = []
        
        def backtrack(idx,combination):
            if len(combination) == k:
                self.combinations.append(combination[:])
                return
            if idx > n:
                return 
            combination.append(idx)
            backtrack(idx + 1 ,combination)
            combination.pop()
            backtrack(idx+ 1 , combination)
            
        backtrack(1, [])
        return self.combinations