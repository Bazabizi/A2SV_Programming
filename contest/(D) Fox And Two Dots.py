import sys
from collections import defaultdict , deque
row , col = map(int, input().split())
grid = []
direction  = [(1,0),(-1,0),(0,1),(0,-1)]
for _ in range(row):
    x = input()
    grid.append(x)
def inbound(row , col , x , y):
    return 0<=row  < x and 0 <= col < y

visited = set()
queue = deque()
colors = set()
for r in range(row):
    for c in range(col):
        colors.add(grid[r][c])
visited = set()
for color in colors:
    for r in range(row):
        for c in range(col):
            if grid[r][c] == color and (r , c) not in visited:
                queue.append([color , (r ,c) , -1])
                visited.add((r , c))
                while queue:
                    cl , direct , parent = queue.popleft()
                    for r , c in direction:
                        r += direct[0]
                        c += direct[1]
                        if inbound(r , c , row , col) and cl == grid[r][c]:
                            if (r , c) in visited:
                                if parent != (r , c):
                                    print("Yes")
                                    sys.exit()
                            else:
                                queue.append([cl , (r , c) , (direct[0] , direct[1])] )
                                visited.add((r, c))

print("No")                                
