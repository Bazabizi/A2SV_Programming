from collections import defaultdict
from collections import Counter

n = int(input())
for _ in range(n):
    size , target = map(int,input().split())
    arr = list(map(int,input().split()))
    left = 0
    right = target
    
    while left + 1 < right:
        mid = left + (right - left)//2
        num = 0
        for i in range(size - 1):
            num += min(mid , arr[i+1] - arr[i])
        num += mid
        
        if num >= target:
            right = mid
        else:
            left = mid
    
    print(right)
     
