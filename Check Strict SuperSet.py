# Enter your code here. Read input from STDIN. Print output to STDOUT
setA=set(map(int,input().split()))
n=int(input())
check=True
for i in range(n):
    setB=set(map(int,input().split()))
    if not setA.issuperset(setB):
         check=False

if check:
    print(True)
else:
    print(False)
