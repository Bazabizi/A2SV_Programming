class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        parent = defaultdict(str)
        count = defaultdict(int)
        for i in range(26):
            char = chr(i + 97)
            parent[char] = char
            count[char] = i
       
        
        def find(child):
            while child != parent[child]:
                parent[child] = parent[parent[child]]
                child = parent[child]
            return child     
        
        def union(x , y):
            rep_x = find(x)
            rep_y = find(y)
            if rep_x != rep_y:
                if count[rep_x] > count[rep_y]:
                    parent[rep_x] = rep_y
                    count[rep_x] = count[rep_y]
                else:
                    parent[rep_y] = rep_x
                    count[rep_y] = count[rep_x]
        length = len(s1)
        for idx in range(length):
            union(s1[idx] , s2[idx])
        ans = ""
     
        for letter in baseStr:
            ans += find(letter)
        return ans