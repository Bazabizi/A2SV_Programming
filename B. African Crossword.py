from collections import defaultdict
row, col = map(int,input().split())

matrix = []

for r in range(row):
    x = input()
        
    matrix.append(x)
rows =[]
for r in range(row):
    compare = defaultdict(int)
    for c in range(col):
        if compare[matrix[r][c]]>0:
            rows.append((r,matrix[r][c]))
        else:
            compare[matrix[r][c]] +=1
column = []
for c in range(col):
    compare = defaultdict(int)
    for r in range(row):
        if compare[matrix[r][c]]>0:
            column.append((c,matrix[r][c]))
        else:
            compare[matrix[r][c]] +=1

for r , val in rows:
    matrix[r]=matrix[r].replace(val,"0")




for r in range(row):
    for c in range(col):
        if (c , matrix[r][c]) in column:
            matrix[r]=matrix[r].replace(matrix[r][c],"0",1)

ans = ""

for r in range(row):
    for c in range(col):
        if matrix[r][c]!= "0":
            ans += matrix[r][c]
print(ans)



            
