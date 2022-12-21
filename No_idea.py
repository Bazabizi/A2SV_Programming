n= list(map(int,input().split()))

new_list= list(map(int,input().split()))
setA=set(map(int,input().split()))
setB=set(map(int,input().split()))

count = 0

for val in new_list:
    if val in setA:
        count+=1
    if val in setB:
        count-=1
print(count)
