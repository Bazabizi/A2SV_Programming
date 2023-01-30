n = int(input())
 
for _ in range(n):
    res = ""
    left = 0
    right = 1
    arr = input()
    if len(arr) == 1:
        print(arr)
    else:
        while right < len(arr):
            if arr[left] != arr[right]:
                res += arr[left]
                right += 1
                left += 1
            else:
                left += 2
                right += 2
        if left == len(arr)-1 and right ==len(arr):
            res += arr[-1]
        a = set(res)
        x = list(a)
        x.sort()
        res = "".join(x)
        print(res)
