k = int(input())
for _ in range(k):
    
    n , m = map(int,input().split())
    grid =[]
    for _ in range(n):
        arr = list(input())
        grid.append(arr)
        
    for col in range(m):
        obs = n
        for row in range(n-1,-1,-1):
            
            if grid[row][col]=="o":
               obs = row
            if grid[row][col] == "*":
                grid[row][col] , grid[obs-1][col] = ".","*"
                obs -= 1
    for row in grid:
        print("".join(row))
