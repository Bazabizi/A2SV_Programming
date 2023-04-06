from collections import defaultdict
n = int(input())
matrix =[]
for _ in range(n):
    x = list(map(int,input().split()))
    matrix.append(x)

source = []
sink = []
for row in range(n):
    for col in range(n):
        if matrix[row][col]==1:
            break
    else:
        sink.append(row + 1)

for row in range(n):
    for col in range(n):
        if matrix[col][row]==1:
            break
    else:
        source.append(row + 1)
print(len(source),*source)
print(len(sink),*sink)
