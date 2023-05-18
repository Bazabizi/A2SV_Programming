class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
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
        temp = []
        for val in equations:
            if val[1:3] == "==":
                union(val[0] , val[3])
            else:
                temp.append(val)
        for val in temp:
            if find(val[0]) == find(val[3]):
                    return False
                
        return True