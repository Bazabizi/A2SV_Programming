row , col , k = map(int,input().split())
 
seats =[]
for  _ in range(row):
    x = input()
    seats.append(x)
ans = 0
for r in range(row):
    count = 0
    for c in range(col):
        if seats[r][c]==".":
            count += 1
        else:
            count = 0
        
        if count >= k:
            ans += 1
            
for c in range(col):
    count = 0
    for r in range(row):
        if seats[r][c]==".":
            count += 1
        else:
            count = 0
        
        if count >= k:
            ans += 1
if k ==1 :
    ans //=2
print(ans)
