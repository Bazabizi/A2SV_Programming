from collections import defaultdict
n= int(input())

for idx in range (n):
    count = defaultdict(int)
    sum = 0
    planet , machine2 = map(int,input().split())
    
    orbits = list(map(int,input().split()))
    
    for num in orbits:
        count[num] += 1
    
    for value in count.values():
        val = min (value, machine2)
        sum += val
    
    print(sum)
        
