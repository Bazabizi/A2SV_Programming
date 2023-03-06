from collections import deque
n = int(input())
for _ in range(n):
    student , divider = map(int,input().split())
    arr = list(map(int,input().split()))
    arr.sort(reverse = True)
    if student < 3:
        print(0)
    else:
        
        total = 2
        count = 0
        for num in arr:
            total += num -1
            count += 1
            if total >= student:
                print(count)
                break
        else:
            print(-1)
    
