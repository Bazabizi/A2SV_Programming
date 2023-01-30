from collections import defaultdict
n = int(input())
for _ in range(n):
    size , target = map(int,input().split())
    arr = list(map(int,input().split()))
    pos = defaultdict(int)
    neg = defaultdict(int)
    for num in arr:
        ans1 = target + num 
        if ans1 in pos:
            print("Yes")
            break
        else:
            pos[num] += 1
        
        ans2 = num - target
        if ans2 in neg:
            print("Yes")
            break
        else:
            neg[num]+=1
    else:
        print("NO")
