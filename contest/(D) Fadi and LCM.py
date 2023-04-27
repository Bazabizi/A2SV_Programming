def combination_check(arr , ans):
    pass
import math
from itertools import combinations
from collections import defaultdict
n = int(input())
val = n
primea  = []
prime = defaultdict(int)
d = 2
while d * d <= n:
    while n %d ==0:
        prime[d] += 1
        primea.append(d)
        n //= d
    d += 1
if n > 1:
   prime[n] += 1
   primea.append(n)
    
ans = []
for key in prime.keys():
    ans.append(key**prime[key])
if len(ans)==1:
    print(1,*ans)
elif len(ans) == 2:
    print(*ans)
else:
    temp = []
    for key , value in prime.items():
        temp.append(key**value)

    ans = (val , 1)
    for i in range(1,len(temp)):
        combo = combinations(temp , i)
        for pro in combo:
            product = math.prod(pro)
            if max(ans) > max(product , val // product):
                ans = (product, val //product)
    
    print(*ans)
