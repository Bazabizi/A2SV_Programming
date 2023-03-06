from collections import deque
n = int(input())
arr = input().split()
queue = deque(arr)
m = int(input())
wait = []
for idx in range(m):
    x = input()
    wait.append([x,idx])

wait.sort()
ans =[]
count = 0
for name,idx in wait:
    while queue and name > queue[0]:
        count += 1
        queue.popleft()
    ans.append([idx,count])

ans.sort()
for idx, count in ans:
    print(count)
