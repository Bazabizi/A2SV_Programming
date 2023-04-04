n = int(input())

for _ in range(n):
    base , num = map(int,input().split())
    x=1
    p = 0
    ans = 0
    while x <= num:
        if x&num:
           ans += base**p
        p += 1
        x <<= 1
    print(ans%(10**9 + 7)) 
