from heapq import heapify  ,heappop , heappush , heappushpop , heapreplace
n = int(input())
for _ in range(n):
    size = int(input())
    arr = list(map(int,input().split()))
    heap = []
    ans = []
    for idx , num in enumerate(arr):
        heappush(heap , (-num, idx))
    
    while len(heap) > 1:
        val1 , idx1 = heappop(heap)
        val2 , idx2 = heappop(heap)
        if val1 != 0 and val2 != 0:
            ans.append((idx2 + 1 , idx1 + 1))
            val1 += 1
            val2 += 1
            if val1 != 0:
                heappush(heap , (val1 , idx1))
            if val2 != 0:
                heappush(heap , (val2 , idx2))
    
    print(len(ans))
    for val in ans:
        print(*val)
