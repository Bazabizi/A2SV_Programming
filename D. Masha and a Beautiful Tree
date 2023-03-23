import math
testcase = int(input ())
def mergeSort(arr, left , right,x):
    if left == right:
        return [ True , 0 , arr[left] ]
    
    mid = left + (right - left)//2
    left_half = mergeSort(arr , left, mid ,  x - 1)
    right_half = mergeSort(arr,mid + 1 , right , x - 1)
    
    if left_half[0] and right_half[0]:
        if abs(left_half[2] - right_half[2]) != 2**(x - 1) or min(left_half[2] , right_half[2])%2 == 0:
            return [False , 0 , 0]
    
        if left_half[2] > right_half[2]:
            return [True , left_half[1]+ right_half[1] + 1, min(left_half[2] , right_half[2])]
        return [True , left_half[1]+ right_half[1] , min(left_half[2] , right_half[2])]
    return [False , 0 , 0]        
        

for _ in range(testcase):
    n = int(input())
    arr = list(map(int,input().split()))
    ans = mergeSort(arr , 0 , n - 1, math.log2(n))
    if not ans[0]:
        print(-1)
    else:
        print(ans[1])
