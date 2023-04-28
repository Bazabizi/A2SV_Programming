import sys
n , target = map(int,input().split())
arr = list(map(int,input().split()))

idx = 0
while idx < n - 1:
    if idx + 1 == target:
        print("YES")
        sys.exit()
    idx += arr[idx]
    if idx + 1 == target:
        print("YES")
        sys.exit()
        
    if idx + 1 > target:
        break


print("NO")
