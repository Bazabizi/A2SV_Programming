from collections import defaultdict
n = int(input())
k = int(input())
count = defaultdict(list)
temp = []
for _ in range(k):
    operation  = list(map(int,input().split()))
    if operation[0] == 1:
        count[operation[1]].append(operation[2])
        count[operation[2]].append(operation[1])
    else:
        temp.append(operation[1])

for num in temp:
    print(*count[num])
