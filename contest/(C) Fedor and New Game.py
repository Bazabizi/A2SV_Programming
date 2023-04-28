n , m , k = map(int,input().split())
arr = []
for _ in range(m + 1):
    arr.append(int(input()))

val = arr[-1]
ans = 0
for num in arr[:-1]:
    count = 0
    for i in range(n):
        if val&(1<<i) != num&(1<<i):
            count += 1
    if count <= k:
        ans += 1

print(ans) 
