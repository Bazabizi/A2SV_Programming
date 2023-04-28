from collections import defaultdict
from collections import Counter
import sys
num , target = map(int,input().split())

ans = [target]
while target > num:
    if target%2==0:
        target = target//2
    elif target %10 == 1:
        target//= 10
    else:
        print("NO")
        sys.exit()
    ans.append(target)

if target == num:
    print("YES")
    print(len(ans))
    print(*ans[::-1])
else:
    print("NO")
