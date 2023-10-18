class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        component = len(strs)
        parent = {idx : idx for idx , word in enumerate(strs)}
        size = {idx : 1 for idx , word in enumerate(strs)}
        
        def checker(word1 , word2):
            count = 0
            for i in range(len(word1)):
                if word1[i] != word2[i]:
                    count += 1
            
            return count
        
        def find(child):
            
            while child != parent[child]:
                parent[child] = parent[parent[child]]
                child = parent[child]
            
            return child
        
        def union(x , y):
            nonlocal component
            repx = find(x)
            repy = find(y)
            
            if repx != repy:
                component -= 1
                if size[repx] >= size[repy]:
                    parent[repy] = repx
                    size[repx] += size[repy]
                else:
                    parent[repx] = repy
                    size[repy] += size[repx]
        
        
        n = len(strs)
        for i in range(n):
            for j in range(i + 1 , n):
                val = checker(strs[i] , strs[j])
                if val <= 2:
                    union(i , j)
        
        return component