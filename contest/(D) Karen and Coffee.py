prefixSum = [0]*(200002)
arr= []
n , k , q = map(int,input().split())
for _ in range(n + q):
    start , end = map(int,input().split())
    if _ >= n:
        arr.append([start,end])
    if _ <n:
        prefixSum[start] += 1
        prefixSum[end+1] -= 1
for idx in range(1,200002):
    prefixSum[idx] += prefixSum[idx-1]
find = []
for idx in range(len(prefixSum)):
    if prefixSum[idx] >= k:
        prefixSum[idx] = 1
        find.append(idx)
    else:
        prefixSum[idx] = 0
ans =[]
find.sort()
for idx in range(1,200002):
    prefixSum[idx] += prefixSum[idx-1]
for start , end in arr:
    x = prefixSum[end]- prefixSum[start-1]
    ans.append(x)
for num in ans:
    print(num)
