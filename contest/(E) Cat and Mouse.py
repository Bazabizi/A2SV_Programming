from collections import defaultdict , deque
row , col , path = map(int,input().split())

grid = []
for _ in range(row):
    x = input()
    grid.append(x)
position = [0 , 0]
for r in range(row):
    for c in range(col):
        if grid[r][c] == "M":
            position = [r, c]
            break
def inbound(row , col , rsize , csize):
    return 0 <= row < rsize and  0 <= col < csize
move = input().split()
visited= set()
ans = -1
for val in move:
    r , c = position
    if val =="1":
        if inbound(r- 1 ,c , row , col ) and grid[r-1][c] =="." or grid[r-1][c] =="M":
            position = [r -1 ,c]    
    elif val =="2":
        if inbound(r+1 ,c , row , col ) and grid[r+1][c] =="." or grid[r+1][c] =="M":
            position = [r + 1 ,c]
    elif val =="3":
        if inbound(r ,c - 1 , row , col ) and grid[r][c - 1] =="." or grid[r][c - 1] =="M":
            position = [r ,c - 1]
    elif val =="4":
        if inbound(r ,c + 1, row , col ) and grid[r][c + 1] =="." or grid[r][c + 1] =="M":
            position = [r ,c + 1]

r , c = position
directions = [(1,0),(-1,0),(0,1),(0,-1)]
queue= deque([(r , c , 0)])
place = set()
while queue:
    r , c ,dis= queue.popleft()
    if dis <= path :
        ans += 1
    for rowadd , coladd in directions:
        rowadd += r
        coladd += c
        if inbound(rowadd, coladd , row ,col) and(rowadd , coladd) not in visited and (grid[rowadd][coladd] == "." or grid[rowadd][coladd] == "M") and dis < path:
            queue.append((rowadd, coladd, dis + 1))
            visited.add((rowadd,coladd))

print(ans)
    
