from collections import defaultdict
n = int(input())
for _ in range(n):
    count = defaultdict(int)
    count["1"] =0
    count["2"] = 0
    count["3"] = 0
    left = 0 
    arr = input()
    size = len(arr)
    found = False
    for right in range (len(arr)):
        char = arr[right]
        if count[char] > 1:
            count[char] += 1
        else:
            count[char] += 1
        
        while min(count.values())>0:
            found = True
            size = min(size,right - left+1)
            count[arr[left]] -=1
            left +=1
    if found :
        print(size)
    else:
        print(0)
