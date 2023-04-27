from itertools import combinations
import math
def gcd(a , b):
    if b == 0:
        return a
    return gcd(b , a% b)

def prime_factorization(num):
    ans = []
    for i in range(1,int(math.sqrt(num)) + 1):
        if num % i == 0:
            ans.append(i)
            ans.append(num//i)
            
    
    return ans
    
n , m = map(int,input().split())

num  = gcd(max(n,m) , min(n,m))
arr = prime_factorization(num)
# for i in range(1 , len(arr)):
#     temp = combinations(arr , i)
    # for comb in temp:
    #     ans.append(math.prod(comb))

arr.sort(reverse = True)
testCase = int(input())

for _ in range(testCase):
    minval , maxVal = map(int,input().split())
    for val in arr:
        if val in range(minval ,maxVal + 1):
            print(val)
            break
    else:
        print(-1)
