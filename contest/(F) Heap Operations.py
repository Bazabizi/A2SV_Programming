from heapq import heapify ,heappop , heappush,heappushpop,heapreplace,_heapify_max ,nlargest ,nsmallest
test = int(input())
heap = []
ans = []
for _ in range(test):
    operation = input()
    if operation[0] == "i":
        ans.append(operation)
        heappush(heap , int(operation.split()[1]))
    elif operation[0] =="r":
        if not heap:
            ans.append("insert 1")
            heappush(heap, -1)
        ans.append(operation)
        heappop(heap)
    else:
        val = int(operation.split()[1])
        while heap and heap[0] < val:
            ans.append("removeMin")
            heappop(heap)
        
        if not heap or heap[0] > val:
            temp = "insert " + str(val)
            ans.append(temp)
            heappush(heap , val)
        ans.append(operation)
        
        
        
        
print(len(ans))
for word in ans:
    print(word)  
