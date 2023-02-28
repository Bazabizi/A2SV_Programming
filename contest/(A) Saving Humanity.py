n = int(input())
for _ in range(n):
    m , k =map(int,input().split())
    k = min(m,k)
    arr = list(input())
    count = 0
    arr.insert(0,"0")
    arr.append("0")
    ans = []
    for _ in range(k):
        count = 0
        for i in range(1,m+1):
            
            if arr[i]=="0" and (arr[i-1]== "1" and arr[i+1]== "0" or arr[i-1]== "0" and arr[i+1]== "1"):
                count += 1
                ans.append(i)
        for idx in ans:
            arr[idx] = "1"
        if count == 0:
            break
   
    print("".join(arr[1:-1]))
