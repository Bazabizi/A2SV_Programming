from collections import defaultdict
n = int(input())
for _ in range(n):
    m = int(input())
    arr= list(map(int,input().split()))
    count = defaultdict(int)
    ans = 0
    for num in arr:
        count[len(bin(num))] += 1
    
    for key, val in count.items():
        if val != 1:
            ans += val*(val - 1) //2
    
    print(ans)
