class Solution:
    def maxProduct(self, words: List[str]) -> int:
        visited = []
        ans = 0
        for word in words:
            count = 0
            for letter in word:
                count |= 1<<(ord(letter) - 97)
            visited.append(count)
        size = len(visited)
        for idx in range(size - 1):    
            
            for idx2 in range(idx + 1 ,size): 
                
                if visited[idx] & visited[idx2] == 0:
                    ans = max(ans, len(words[idx]) * len(words[idx2]))
        
        return ans