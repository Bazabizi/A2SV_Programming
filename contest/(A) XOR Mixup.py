from collections import defaultdict
from collections import Counter
n = int(input())
for _ in range(n):
    size = input()
    arr = list(map(int,input().split()))
    ans = 0
    temp = set()
    for num in arr:
        ans^= num
        if num in temp:
            print(num)
            break
        
        temp.add(ans)
    
