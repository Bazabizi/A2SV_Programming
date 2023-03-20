from collections import defaultdict
from collections import Counter
n , power = map(int,input().split())
arr = list(map(int,input().split()))
arr.sort()

length = n
ans = 0
if length == 1 and power > arr[-1]:
    print(ans)
else:
    sum = 0
    i = -1
    while length > 0:
        sum += arr[i]
        if sum > power:
            ans += 1
            sum = 0
            i -= 1
        length -=1
    print(ans)
       
