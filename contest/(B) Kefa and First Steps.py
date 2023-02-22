n = int(input())
money = list(map(int,input().split()))
ans = 0
count = 1
found = False
for idx in range(n -1):
    if money[idx] <= money[idx+1]:
        count += 1
        found = True
    else:
        count =1
    ans = max(ans,count)
if found:
    print(ans)
else:
    print(1)
