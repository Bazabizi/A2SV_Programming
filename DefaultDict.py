# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import defaultdict
n,m=map(int ,input().split())
d=defaultdict(list)

for idx in range(n):
    x=input()
    d[x].append(idx+1)
    
for idx in range(m):
    x=input()
    if x in d:
        print(*d[x])
    else:
        print(-1)
    
