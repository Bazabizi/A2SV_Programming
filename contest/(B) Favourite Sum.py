test = int(input())
for _ in range(test):
    n , x = map(int,input().split())
    arr = sorted(list(map(int,input().split())))

    total = x*(1 + x)//2
    
    for num in arr:
        if num <=x:
            total -= 2*num
    
    print(total)
