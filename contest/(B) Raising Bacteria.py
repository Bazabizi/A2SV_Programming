from collections import defaultdict
from collections import Counter
n = int(input())
if n&(n-1)==0:
    print(1)
else:
    ans = 1
    while n > 1:
        if n%2==1:
            ans += 1
            n -= 1
        n >>= 1
    print(ans )

    
