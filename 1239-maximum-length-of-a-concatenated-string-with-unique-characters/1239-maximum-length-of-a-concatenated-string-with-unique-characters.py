class Solution:
    def noRepeat(self,first , second):
        newString = "".join(first) + second
        ans = max(Counter(newString).values())
        return ans == 1
    def maxLength(self, arr: List[str]) -> int:
        self.ans = 0
        def backtrack(idx , current):
            if idx >= len(arr):
                return
            
            if self.noRepeat(current , arr[idx]):
                current.append(arr[idx])
                self.ans = max(self.ans , len("".join(current)))
                
                backtrack(idx + 1 , current)
                current.pop()
            backtrack(idx + 1, current)
        
        backtrack(0 , [])
        return self.ans
        