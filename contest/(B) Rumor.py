from collections import defaultdict , deque
n , pair = map(int,input().split())
graph = defaultdict(list)
gold = list(map(int,input().split()))

for _ in range(pair):
    start , end = map(int,input().split())
    graph[start].append(end)
    graph[end].append(start)
    
queue = deque()
ans = 0
visited = set()
for val in graph:
    
    price = gold[val - 1]
    if val not in visited:
        queue.append((val , gold[val-1]))
        visited.add(val)
        while queue:
            val , price1 = queue.popleft()
            for num in graph[val]:
                if num not in visited:
                    if price  > gold[num - 1]:
                        price = gold[num - 1]
                    queue.append((num , price))
                    visited.add(num)
        ans += price

for i in range(n):
    if i+ 1 not in visited:
        ans += gold[i]
print(ans)
