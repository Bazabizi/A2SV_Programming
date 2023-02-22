n = int(input())
skill = list(map(int,input().split()))
 
skill.sort()
ans = 1
right = 1
for left  in range(n-1):
    while right<n and skill[right] -skill[left] <= 5:
        right +=1
     
    ans = max(ans,right-left)
    
print(ans)
