
def compareSize(size1,size2):
    order=["X","L","M","S"]
    size = min(len(size1),len(size2))-1
   
    left , right=len(size1)-1 , len(size2)-1
    while 0<=size:
        if order.index(size1[left]) > order.index (size2[right]):
             return "<"
         
        elif order.index(size1[left]) < order.index (size2[right]):
            return ">"
        
        size -= 1
        left -=1
        right-=1
    
    if len(size1)==len(size2):
        return "="
    
    elif len(size1)>len(size2) and size1[-1]=="L":
        return ">"
    elif len(size1)<len(size2) and size1[-1]=="S":
        return ">"
    else:
        return "<"


    
n = int(input())

for idx in range(n):
    t_shirt1 ,t_shirt2=input().split()
    
    print(compareSize(t_shirt1,t_shirt2))


    
