from heapq import heapify  ,heappop , heappush , heappushpop , heapreplace

test = int(input())
for _ in range(test):
    n , m = map(int,input().split())
    narr = (list(map(int,input().split())))
    marr = (list(map(int,input().split())))
    heapify(narr)
    for num in marr:
        heapreplace(narr , num)
    
    print(sum(narr))
    
