n = int(input())
arr = list(map(int,input().split()))
count = 0
temp = []
for idx,num in enumerate(arr):
    temp.append([num , False])

for idx , num in enumerate(arr):
    if arr[arr[arr[num - 1]- 1] - 1] == arr[idx]:
        print("YES")
        break
else:
    print("NO")
    
