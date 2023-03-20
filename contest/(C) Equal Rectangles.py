from collections import defaultdict
from collections import Counter
n = int(input())

for _ in range(n):
    n  = int(input())
    arr = list(map(int,input().split()))
    arr.sort()
    ans = 0
    left = 0 
    right = 4*n -1
    area = arr[0]*arr[-1]
    while left <= right:
        if arr[left]!= arr[left + 1] or arr[right] != arr[right-1]:
            print("NO")
            break
        if arr[right]*arr[left] !=  area:
            print("NO")
            break
        left +=2
        right -= 2
    else:
        print("YES")
