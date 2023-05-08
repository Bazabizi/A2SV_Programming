from collections import deque, defaultdict
import sys
n = int(input())
directions = [(1, -1) ,(0,-1),(0,1),(1,1),(-1,-1),(1,0),(-1,0),(-1,1) ]
def inbound(row , col , size):
    return 0 <= row < 3 and 0 <= col <= size

for _ in range(n):
    
    size = int(input())
    arr = []
    arr.append(input())
    arr.append(input())
    queue = deque([(1, 1)])
    visited = set()
    
    while queue:
        row , col = queue.popleft()
        if row == 2 and col == size:
            print("YES")
            break
        for r , c in directions:
            r += row 
            c += col
            if inbound(r , c , size) and (r , c) not in visited and arr[r- 1][c- 1] == "0":
                queue.append((r, c))
                visited.add((r, c))
    else:
        print("NO")            
