class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        ans = []
        count = defaultdict(int)
        size = len(s)
        for index in range(size):
            count[s[index]] = index
        maxDistance = 0
        length = 0
        
        for idx in range(size):
            if maxDistance < count[s[idx]]:
                maxDistance = count[s[idx]]
            length +=1
            if maxDistance == idx:
                ans.append(length)
                maxDistance = 0
                length = 0
            
        
        return ans