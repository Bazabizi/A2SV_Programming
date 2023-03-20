from collections import defaultdict

n , k = map(int,input().split())
arr = list(map(int,input().split()))
find = defaultdict(int)
count = False
left = 0
ans = []
maxVal = 0
for right , num in enumerate(arr):
    find[num] += 1
    
    while len(find) > k  and left < n:
        find[arr[left]] -= 1
        if find[arr[left]]== 0:
            find.pop(arr[left])
        left += 1
    
    if len(find) == k:
        count = True
        window  = right - left + 1
        if window > maxVal:
            maxVal = window
            ans =[left + 1 , right + 1] 

# ans.sort()
# print(ans)
if count:
    print(ans[0] , ans[1])
else:
    print(1 ,len(arr) )
