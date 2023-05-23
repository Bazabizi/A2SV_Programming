class Solution:
    def maximumSegmentSum(self, nums: List[int], removeQueries: List[int]) -> List[int]:
        total = defaultdict(int)
        size = len(nums)
        temp = [0]*size
        ans = [0]
        maxval = 0
        parent = { i:i for i in range(size)}
        count = { i:1 for i in range(size)}
        
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
                    total[rep_x] += total[rep_y]
                else:
                    parent[rep_x] = rep_y
                    count[rep_y] += count[rep_x]
                    total[rep_y] += total[rep_x]
        
        for idx , val in enumerate(removeQueries[::-1]):
            if val != 0:
                if temp[val-1] != 0:
                    union(val , val - 1)                
            
            if val != size - 1:
                if temp[val + 1] != 0:
                    union(val , val + 1)                
            
            temp[val] = nums[val]
            rep = find(val)
            total[rep] += nums[val]
            maxval = max(total[rep] , maxval)
            ans.append(maxval)
        
        ans = ans[::-1]
        return ans[1:]