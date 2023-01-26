size1 , size2 = (map(int,input().split()))
arr1 = list(map(int,input().split()))
arr2 = list(map(int,input().split())) 

idx1 = 0
idx2 = 0
ans = []

while idx1<size1 and idx2 < size2:
    if arr1[idx1] <= arr2[idx2]:
        ans.append(arr1[idx1])
        idx1 +=1
    else:
        ans.append(arr2[idx2])
        idx2 +=1

ans.extend(arr1[idx1:])
ans.extend(arr2[idx2:])
print(*ans)
