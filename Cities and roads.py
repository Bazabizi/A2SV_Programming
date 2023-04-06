from collections import defaultdict
n = int(input())
count = defaultdict(list)
ans = []
for _ in range(n):
    x = list(map(int,input().split()))
    ans.append(x)
count = 0
for row in range(n):
    for col in range(n):
        if ans[row][col]==1:
            count += 1

print(count//2)
