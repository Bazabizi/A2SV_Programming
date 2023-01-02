n , k = map(int,input().split())
 
theory = list(map(int,input().split()))
sleep  = list(map(int,input().split()))
size= len(sleep)
total=0
max_val=0
 
for idx in range(size):
    if sleep[idx]==1 :
        total += theory[idx]
 
i=0
j=0
while j < size :
    if sleep[j]==0:
        total += theory[j]
    
    if j-i >=k:
        if sleep[i]==0:
            total -= theory[i]
        i += 1
    max_val = max(max_val, total)
    j += 1
 
print(max_val)
