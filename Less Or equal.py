n , k = map(int,input().split())
 
arr = list(map(int,input().split()))
arr.sort()
 
if k > n :
    print(-1)
elif k==n:
    print(arr[k-1])
    
else:
    if k == 0:
        if arr[k]>1:
            print(arr[k]-1)
        else:
            print(-1)
    elif arr[k-1] != arr[k]:
        print(arr[k-1])
    else:
        print(-1)
