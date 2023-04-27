from collections import defaultdict
import math
n , k = map(int,input().split())
arr = list(map(int,input().split()))
def simplified(num , k):
    temp = defaultdict(int)
    n = 2
    ans = [1]
    total = [1]
    while n*n <= num:
        while num %n ==0 :
            temp[n] += 1
            num //= n
        n += 1
    if num > 1:
        temp[num] += 1
    for key,value in temp.items():
        if value % k==0:
            ans.append(1)
            total.append(1)
        else:
            ans.append(key**(k - (value%k)))
            total.append(key**(value%k))
    return math.prod(ans) , math.prod(total)
count = defaultdict(int)
ans = 0
for num in arr:
    
    val = simplified(num , k)
    if val[0] in count:
        ans += count[val[0]]

    count[val[1]] += 1

print(ans)
