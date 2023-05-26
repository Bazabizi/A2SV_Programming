import sys
from collections import defaultdict
n, m = map(int, input().split())
visited = defaultdict(int)
edge = []
graph = defaultdict(list)
for _ in range(m):
    start ,  end = map(int,input().split())
    edge.append((start , end))
    graph[start].append(end)
    graph[end].append(start)
stack = [(1 , 1)]
while stack:
    vertix , color = stack.pop()
    visited[vertix] = color
    for val in graph[vertix]:
        if val not in visited:
            stack.append((val , -color))
        else:
            if visited[val] == color:
                print("NO")
                sys.exit()

print("YES")
for left , right in edge:

    print(1 if visited[left] == 1 else 0, end="")
