t = int(input())
for _ in range(t):
    n = int(input())
    
    
    arr = list(map(int,input().split()))
    minVal = arr[0]
    for idx in range(n):
        minVal &= arr[idx]
    print(minVal)
