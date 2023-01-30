m = int(input())
for i in range(m):
    n, k = map(int,input().split())
    
    arr = list(map(int,input().split()))
    count = 0
    ans = 0
    idx = 0
    while idx < n-1 :
        if arr[idx]*2**i <arr[idx+1]*2**(i+1):
            count +=1
        else:
            count = 0
        if count>k-1:
            ans += 1
        idx +=1
    print(ans)
