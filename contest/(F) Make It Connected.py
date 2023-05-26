from collections import defaultdict ,deque 
from heapq import heapify , heappop,heappush,heappushpop,heapreplace

def find(child):
    if child != parent[child]:
        parent[child] = find(parent[child])
    return parent[child]
    
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
        return True
    return False

n , m = map(int , input().split())
parent = {i :i for i in range(1, n + 1)}
count = {i :1 for i in range(1 , n + 1)}
arr = list(map(int,input().split()))
heap = []
idx = 0
val = float('inf')

for idx2 , num in enumerate(arr):
    if val > num:
        idx = idx2
        val = num

for idx2 , num in enumerate(arr):
    if idx2 != idx:
        temp = (val + num , idx + 1 , idx2+ 1)
        # heappush(heap , temp)
        heap.append(temp)
        
for _ in range(m):
    start , end , k = map(int , input().split())
    # heappush(heap , (k , start , end))
    heap.append((k, start, end))

heap.sort()
ans = 0
for i in range(len(heap)):
    val, start, end = heap[i]
    flag = union(start, end)
    if flag:
        ans += val
# while heap:
#     val , end , start = heappop(heap)
#     flag = union(start , end)
#     if flag:
#         ans += val
    
print(ans)
