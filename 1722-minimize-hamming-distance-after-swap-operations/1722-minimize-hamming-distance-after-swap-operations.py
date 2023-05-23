class Solution:
    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:
        size = len(source)
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
        
        for start , end in allowedSwaps:
            union( start, end )
        
        temp = defaultdict(lambda:defaultdict(int))
        for idx ,val in enumerate(source):
            p = find(idx)
            temp[p][val] += 1
        
        ans = 0
        for idx , val in enumerate(source):
            p = find(idx)
            target_val = target[idx]
            if temp[p][target_val] < 1:
                ans += 1
            temp[p][target_val] -= 1
        
        return ans