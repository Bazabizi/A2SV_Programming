from collections import defaultdict
comp=[]
n,m = map(int,input().split())
result = 0
 
for idx in range(n):
    answer = input()
    comp.append(answer)
mark=list(map(int,input().split()))
 
for col in range(m):
    compare= defaultdict(int)
    
    for row in range(n):
        compare[comp[row][col]]+=1
    
    result += max(compare.values())*mark[col]
 
print(result)
    
