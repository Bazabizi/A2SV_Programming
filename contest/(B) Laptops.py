n = int(input())
qua =[]
temp = []
for i in range(n):
    a, b = map(int,input().split())
    temp.append((a,b))
temp.sort()
for num , i in temp:
    qua.append(i)
for i in range(len(qua)-1):
    if qua[i] > qua[i+1]:
        print("Happy Alex")
        break
else:
    print("Poor Alex")
