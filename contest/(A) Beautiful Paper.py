
n = int(input())
 
for i in range(n):
    
    a , b = map(int,input().split())
    c,d = map(int,input().split())
    
    if a == b:
        print("No")
    else:
        if a ==c and b+ d ==a:
            print("Yes")
        elif a ==d and b+ c ==a:
            print("Yes")
        elif b ==c and a+ d ==b:
            print("Yes")
        elif b == d and a + c ==b:
            print("Yes")
        else :
            print("No")
