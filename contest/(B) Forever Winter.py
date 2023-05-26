from collections import defaultdict , deque
import sys
test = int(input())
for _ in range(test):
    n , m = map(int , input().split())
    graph = defaultdict(list)
    for __ in range(m):
        start , end = map(int ,input().split())
        graph[start].append(end)
        graph[end].append(start)
    visited = defaultdict(int)
    for val in graph:
        visited[len(graph[val])] += 1
    
    visited.pop(1)
    if len(visited) == 1:
        
        print(max(visited.keys()) , max(visited.keys()) - 1)
    else:
        ans = []
        for val in visited:
            ans.append([visited[val] , val])
        ans.sort()
        print(ans[0][1] , ans[1][1] - 1) 
        
