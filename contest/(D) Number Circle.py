n = int(input())
check = True
 
temp = [0]*n
 
arr = list(map(int,input().split()))
arr.sort()
 
left = 0
right = len(arr) -1
idx = len(arr) -1
while idx>-1:
    temp[right] = arr[idx]
    right -=1
    idx -=1
    if idx >-1:
        temp[left] = arr[idx]
        left +=1
        idx -=1
 
if temp[0] >= temp[1]+ temp[-1]:
    check = False
if temp[-1] >= temp[-2] + temp[0]:
    check = False
if check:
    for i  in range(1,len(temp)-1):
        if temp[i]>= temp[i-1] + temp[i+1]:
            check = False
            break
 
if check:
    print("YES")
    print(*temp)
else:
    print("NO")
