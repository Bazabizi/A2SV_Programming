n = int(input())
arr = list(map(int,input().split()))
wube = 0
hen = 0
left = 0
right = n -1
 
while left <= right :
    if left <= right and arr[left]> arr[right]:
        wube += arr[left]
        left +=1
    elif left <= right and arr[right] >= arr[left]:
        wube += arr[right]
        right -=1
    if left <= right and arr[left]>arr[right]:
        hen += arr[left]
        left +=1
    elif left <= right and arr[left] <=arr[right]:
        hen +=arr[right]
        right -=1
 
print(wube, hen)
