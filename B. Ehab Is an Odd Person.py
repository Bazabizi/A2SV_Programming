n = int(input())

arr = list(map(int,input().split()))
even = False
odd = False
for num in arr:
    if num %2 :
        even = True
    else:
        odd = True
if odd and even:
    arr.sort()
print(*arr)
