from collections import defaultdict , deque
parent = defaultdict(str)
count =defaultdict(int)
for i in range(26):
    char = chr(i + 97)
    parent[char] = char
    count[char] += 1
    
def find(child):
        while child != parent[child]:
            parent[child] = parent[parent[child]]
            child = parent[child]
        return child     
        
def union(x , y):
    rep_x = find(x)
    rep_y = find(y)
    if rep_x != rep_y:
        if count[rep_x] > count[rep_y]:
            parent[rep_x] = rep_y
            count[rep_y] += count[rep_x]
        else:
            parent[rep_y] = rep_x
            count[rep_x] += count[rep_y]
n = int(input())
name1 = input()
name2 = input()
visited= set()

for i in range(n):
    union(name1[i] , name2[i])
    visited.add(name1[i])
    visited.add(name2[i])
ans = []
for val in visited:
    name = find(val)
    if val != name:
        ans.append([name , val])
    
    
print(len(ans))
for val in ans:
    print(*val)
