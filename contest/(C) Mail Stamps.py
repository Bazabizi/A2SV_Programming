import sys
from collections import defaultdict
graph = defaultdict(list)
visited = set()
n = int(input())
for _ in range(n):
    start  , end = map(int,input().split())
    graph[start].append(end)
    graph[end].append(start)
    visited.add(start)
    visited.add(end)
elements = len(visited)

visited= set()
count = 0
start = 1
for val in graph:
    if len(graph[val]) == 1:
        start = val
        break
count = 0
ans = set()
stack = [start]
while stack:
    temp = stack.pop()
    if temp not in ans:
        ans.add(temp)
        count += 1
    if count == elements:
        print(*list(ans))
        sys.exit()
    for val in graph[temp]:
        if val not in ans:
            stack.append(val)

