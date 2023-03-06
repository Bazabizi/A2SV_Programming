n = int(input())
for _ in range(n):
    
    walk , ele , now = map(int,input().split())
    time = (4*ele + now*ele) 
    walk_and_lift = now*walk + (4-now)*ele
    time = min(4*walk,time , walk_and_lift)
        
    
    print(time)
