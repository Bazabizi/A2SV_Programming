from collections import defaultdict , deque
n , m = map(int , input().split())
parent = {i:i for i in range(1 ,n +  1)}
count = {i : 1 for i in range(1 , n + 1)}
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
            count[rep_y] += count[rep_x]
        else:
            parent[rep_y] = rep_x
            count[rep_x] += count[rep_y]
    
 

for _ in range(m):
    arr = list(map(int , input().split()))
    if len(arr) > 2:
        
        for idx in range(1 , len(arr) - 1):
           union(arr[idx] , arr[idx + 1])
ans = []
for i in range(1 , n + 1):
    c = find(i)
    ans.append(count[c])
print(*ans)
