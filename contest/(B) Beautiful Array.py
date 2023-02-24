from collections import defaultdict
n = int(input())
arr = list(map(int,input().split()))
pos =[]
neg =[]
zero =[]
for num in arr:
    if num <0:
        neg.append(num)
    elif num > 0:
        pos.append(num)
    else:
        zero.append(num)
    
print (1, neg[0])
if len(pos)==0:
    print(2, neg[1], neg[2])
    size = len(neg) -3 + len (zero)
    print(size,end=" ")    
    for i in range(3,len(neg)):
        print(neg[i],end=" ")
    for i in range(1,len(pos)):
        print(pos[i],end=" ")
    for i in range(len(zero)):
        print(zero[i])
else:
    print(1,pos[0])
    size = len(neg) -1 + len(pos)-1 + len (zero)
    print(size,end=" ")
 
    for i in range(1,len(neg)):
        print(neg[i],end=" ")
    for i in range(1,len(pos)):
        print(pos[i],end=" ")
    for i in range(len(zero)):
        print(zero[i])
    
