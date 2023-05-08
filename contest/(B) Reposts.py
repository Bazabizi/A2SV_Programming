from  collections import defaultdict , deque
n = int(input())
graph = defaultdict(list)
for _ in range(n):
    posts = input()
    arr = (posts.lower()).split()
    graph[arr[2]].append(arr[0])
    
queue = deque([("polycarp"  , 1)])
visited = set()
maxVal = 1
while queue:
    name , post = queue.popleft()
    maxVal = max(maxVal , post)
    for val in graph[name]:
        if (val , name) not in visited:
            queue.append((val , post + 1))
            visited.add((val , name))
print(maxVal)
