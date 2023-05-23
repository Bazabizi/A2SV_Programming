class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        size = len(s)
        parent = {i : i for i in range(size)}
        count = {i : 1 for i in range(size)}
        
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
                    parent[rep_y] = rep_x
                    count[rep_x] += count[rep_y]
                else:
                    parent[rep_x] = rep_y
                    count[rep_y] += count[rep_x]
        for start , end in pairs:
            union(start , end)
        temp = defaultdict(list)
        for idx , letter in enumerate(s):
            p = find(idx)
            heappush(temp[p] , letter)
        
        ans = ""
        for idx, letter in enumerate(s):
            p = find(idx)
            ans += heappop(temp[p])
        
        return ans