n , m = map(int,input().split())
arr1= list(map(int,input().split()))
arr2=list(map(int,input().split()))
top = 0 
bottom = 0
count = 0
ans =[]
while bottom < m:
    if top<n and arr2[bottom] > arr1[top]:
        count += 1
        top +=1
    else:
        ans.append(count)
        bottom +=1
print(*ans)
