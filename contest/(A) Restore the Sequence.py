n = int(input())
for _ in range(n):
    m = int(input())
    arr = list(map(int,input().split()))
    ans =[]
    
    left = 0
    right = m - 1
    while left <= right :
        ans.append(arr[left])
        if right != left:
            ans.append(arr[right])
        right -=1
        left +=1
    print(*ans)
