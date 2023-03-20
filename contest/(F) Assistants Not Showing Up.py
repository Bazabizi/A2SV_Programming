n , test_cases = map(int,input().split())
prefixSum = [0]* (n + 1)
for _ in range(test_cases):
   start , end = map(int,input().split())
   prefixSum[start] += 1
   prefixSum[end + 1] -= 1

for idx in range(1,n):
    prefixSum[idx] += prefixSum[idx -1]

for num in prefixSum[:-1]:
    if num ==0:
        print("YES")
        break
else:
    print("NO")
