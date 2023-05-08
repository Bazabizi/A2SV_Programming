import sys
from collections import defaultdict ,deque
startx , starty , endx , endy = map(int,input().split())
n = int(input())
directions = [(0, -1),(1, 0),(-1 , 0),(0 ,1) , (1,1),(-1,1),(1,-1) , (-1,-1)]

def inbound(row , col):
    return 0 <= row < 10**9 and 0 <= col < 10**9
     
possible = defaultdict(list)
for _ in range(n):
    r , a , b = map(int,input().split())
    possible[r- 1].append((a-1 , b-1))
    
visited = set((startx - 1 , starty - 1))
queue = deque([(startx-1 , starty- 1 , 0)])
while queue:
    row , col , path = queue.popleft()
    for r , c in directions:
        r += row 
        c += col
        if inbound(r , c) and (r , c) not in visited:
            
            visited.add((r , c))
            for min_col , max_col in possible[r]:
                if min_col <= c <= max_col:
                    queue.append((r , c, path + 1))
                    if (r + 1 , c + 1) == (endx , endy):
                        print(path + 1)
                        sys.exit()
print(-1)
