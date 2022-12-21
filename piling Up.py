# Enter your code here. Read input from STDIN. Print output to STDOUT
n=int(input())
for x in range(n):
    m=int(input())
    block=list(map(int ,input().split()))
    check=True
    l=0
    r=len(block)-1
    while(l<r):
        large=max(block[l],block[r])
        if block[l]>block[r]:
            l+=1
        else:
            r-=1
        if block[l]>large or block[r]>large:
            check=False
            break
    if check:
        print("Yes")
    else:
        print("No")
