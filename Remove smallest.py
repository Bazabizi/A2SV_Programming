n = int (input())
for i in range(n):
    size = int(input())
    arr = list(map(int,input().split()))
    arr.sort()
    for i in range(size-1):
        if arr[i+1] - arr[i] >1:
            print("NO")
            break
    else:
        print("YES")
