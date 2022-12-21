# Enter your code here. Read input from STDIN. Print output to STDOUT
room={}
n=int(input())
m=input().split()

for i in m:
    room[i] =1+room.get(i,0)
    
for key in room:
    if room[key]==1:
        print(key)
