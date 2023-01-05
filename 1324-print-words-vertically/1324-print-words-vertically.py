class Solution:
    def printVertically(self, s: str) -> List[str]:
        words = s.split()
        count= defaultdict(int)
        
        for val in words:
            count[val] = len(val)
        
        element = max (count.values())
        size = len(words)
        ans=[]
        
        for col in range(element):
            temp=""
            for row in range(size):
                if col < len(words[row]):
                    temp += words[row][col]
                else:
                    while row < size :
                        if col < len(words[row]):
                            temp += " "
                            break
                        else:
                            row +=1
            ans.append(temp)
        
        return ans
                