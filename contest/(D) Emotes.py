from collections import defaultdict
from collections import Counter
n , m , k = map(int,input().split())

arr = list(map(int,input().split()))
arr.sort()
ans = 0
if len(arr) == 1:
    ans = arr[-1] * min(k,m)
else:
    product = m // (k+1)
    reme = m % (k +1)
    ans = ((product * k) + reme) * arr[-1]
    ans += product * arr[-2]
print(ans)
