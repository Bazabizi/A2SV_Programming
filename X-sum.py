from collections import defaultdict
n = int(input())
for _ in range(n):
    maxVal = 0
    sumOf = defaultdict(int)
    diffOf = defaultdict(int)
    row,col = map(int,input().split())
    matrix = []
    for i in range(row):
        arr = list(map(int,input().split()))
        matrix.append(arr)
    
    for r in range(row):
        for c in range(col):
            diffOf[c-r] += matrix[r][c]
    for r in range(row):
        for c in range(col):
            sumOf[c+r] += matrix[r][c]
    
    for r in range(row):
        for c in range(col):
            ans = diffOf[c-r] + sumOf[c+r] - matrix[r][c]
            maxVal = max(maxVal, ans)
    
    print(maxVal)
