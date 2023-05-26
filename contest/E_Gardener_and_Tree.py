from collections import defaultdict , deque
test = int(input())
for _ in range(test):
    input()
    n , k = map(int, input().split())
    queue = deque()
    graph = defaultdict(list)
    indegree = defaultdict(int)
    visited = set()
    checked = set()
    
    
    for __ in range(n - 1):
        start , end = map(int , input().split())
        graph[start].append(end)
        graph[end].append(start)
        indegree[start] += 1        
        indegree[end] += 1    
            
    for i in range(1 , n + 1):
        if indegree[i] == 1 or indegree[i] == 0:
            queue.append(i)
            visited.add(i)
    temp = 0
    while queue and k > 0:
        size = len(queue)
        temp += size
        for x in range(size):
            vertix = queue.popleft()
            for val in graph[vertix]:
                if val not in visited:
                    indegree[val] -= 1
                    if indegree[val] == 1:
                        visited.add(val)
                        queue.append(val)
            
        k -= 1
    print(n - temp)
