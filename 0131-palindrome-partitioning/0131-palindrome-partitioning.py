class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans = []
        pali = defaultdict(bool)
        def backtrack(idx , path):
            if idx >= len(s):
                ans.append(path[:])
                return
            
            for i in range(idx  , len(s)):
                if pali[(idx,i)]:
                    path.append(s[idx:i+1])
                    backtrack(i + 1 , path)
                    path.pop()
        
        for i in range(len(s)):
            pali[(i , i)] = True
        for i in range(len(s) - 1):
            val = False
            if s[i] == s[i+1]:
                val = True
            pali[(i , i+1)] = val
        
        for i in range(2 , len(s)):
            start = 0
            for j in range(i,len(s) ):
                val = False
                if s[j] == s[start] and pali[(start + 1 , j - 1 )]:
                    val = True
                pali[(start , j)] = val
                start += 1
        
        backtrack(0 , [])
        return ans
                
        