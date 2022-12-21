# Enter your code here. Read input from STDIN. Print output to STDOUT
n=int(input())
check={}
while n>0:
    x=input()
    check[x]=check.get(x,0)+1
    n-=1
print(len(check))
for val in check.values():
     print(val,end=" ")
