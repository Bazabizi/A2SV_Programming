from collections import defaultdict
n , m = map(int,input().split())
name = []
graph = defaultdict(bool)
visited = defaultdict(int)
for _ in range(n):
    name.append(input())
for _ in range(m):
    a , b = input().split()
    graph[(a , b)] = True
    graph[(b , a)] = True

temp = []
for i in range(1 , 2**n):
    arr = []
    for j in range(len(name)):
     
        if i& 1<<j:
            arr.append(name[j])
    
    for i in range(len(arr)):
        flag = False
        for j in range(len(arr)):
            if (arr[i] , arr[j]) in graph:
                flag = True
                break
        if flag:
            break
    else:
        if len(temp) < len(arr):
            temp = arr

print(len(temp))
temp.sort()
for name in temp:
    print(name)
            