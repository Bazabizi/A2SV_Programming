n=int(input())
list1= list(map(int,input().split()))
max_val=list1[0]
min_val= list1[0]
count=0
for num in list1:
    if max_val < num:
        count += 1
        max_val=num
        
    elif min_val > num:
        count += 1
        min_val = num
        
print(count)
