n = int(input())
for _ in range(n):
    length = int(input())
    arr = sorted(list(map(int,input().split())))
    temp = []
    idx = 0
    ans = sum(arr)
    for idx , num in enumerate(arr):
            temp = 0
            val = arr[idx]
            for idx2 , num in enumerate(arr):
                if idx2 != idx:
                    while num &1 == 0:
                        num >>= 1
                        val <<= 1
                    temp += num
            temp += val
            ans = max(temp ,ans)
    
    print(ans)
