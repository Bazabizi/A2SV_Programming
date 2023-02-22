from collections import defaultdict
n , m = map(int,input().split())
price = list(map(int,input().split()))
 
price.sort()
count = defaultdict(int)
for _ in range(m):
    count[input()] += 1
 
arr = []
for key,value in count.items():
    x = value
    arr.append(x)
buy = 0
ans1 = 0
arr.sort(reverse = True)
index = 0
for num in arr:
    ans1 += price[index]*num
    index += 1
 
index = n - 1
ans2 = 0
for num in arr:
    ans2 +=  price[index] *num
    index -= 1
print(ans1,ans2)
