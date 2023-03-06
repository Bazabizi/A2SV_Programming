class Solution:
    def smallestCharacterOccurance(self,s):
        word = list(s)
        word.sort()
        letter = Counter(word)
        return letter[word[0]]
            
        
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        length = len(words)
        
        for idx in range(length):
            words[idx] = self.smallestCharacterOccurance(words[idx])
        
        words.sort()
        size = len(queries)

        for idx in range(size):
            value = self.smallestCharacterOccurance(queries[idx])
            
            #bisect_right
            
            left = -1
            right = length
            
            while left + 1 < right:
                mid = left + (right - left) // 2
                
                if value < words[mid]:
                    right = mid      
                else:
                    left = mid
            queries[idx] = length - right
        
        return queries
            