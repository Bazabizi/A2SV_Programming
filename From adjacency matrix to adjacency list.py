from collections import defaultdict
n = int(input())
count = defaultdict(list)
ans = []
for _ in range(n):
    x = list(map(int,input().split()))
    ans.append(x)
for row in range(n):
    for col in range(n):
        if ans[row][col]==1:
            count[row+1].append(col + 1)
            
for value in count.values():
    print(len(value),*value)
