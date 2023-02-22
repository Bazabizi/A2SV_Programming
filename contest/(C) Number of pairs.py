numberOfBoys= int(input())
boys = list(map(int,input().split()))
 
numberOfGirls= int(input())
girls = list(map(int,input().split()))
 
boys.sort()
girls.sort()
b =0 
g =0
ans = 0
while b < numberOfBoys and g< numberOfGirls:
    if abs(boys[b] - abs(girls[g])) <= 1:
        ans +=1
        b += 1
        g += 1
    else:
        if boys[b] < girls[g]:
            b += 1
        else:
            g += 1
 
print(ans)
