n = int(input())
 
def compare (real, temp):
    for i in range(len(temp)):
        if real[i]!= temp[i]:
            return False
    return True
    
arr = list(map(int,input().split()))
temp= arr.copy()
temp.sort()
temp2 =[]
idx = 0
idx2 = 0 
for i in range(len(arr)):
    if arr[i]!= temp[i]:
        idx = i
        break
    
for i in range(len(arr)-1,-1,-1):
    if arr[i]!= temp[i]:
        idx2 = i
        break
x = arr[idx:idx2+1]
x.reverse()
temp2 = arr[:idx] + x + arr[idx2+1:] 
if compare(temp2,temp):
    print("yes")
    print(idx+1,idx2+1)
else:
    print("no")
