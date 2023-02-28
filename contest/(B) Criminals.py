n = int(input())
for _ in range(n):
    m =int(input())
    arr = list(map(int,input().split()))
    ans = 0
    find = True
    for idx in range(m-1):
        if find:
            if arr[idx] != 0:
                index = idx
                find = False
        ans += arr[idx]
        if not find:
            if arr[idx] ==0:
                ans += 1
    
    print(ans)
