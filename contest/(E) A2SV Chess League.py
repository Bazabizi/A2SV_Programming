n , target = map(int,input().split())
arr = list(map(int,input().split()))
def mergeSort(arr,left,right,target):
    if left == right:
        return [left]
    mid = left + (right- left)//2
    left_half = mergeSort(arr,left , mid ,target)
    right_half = mergeSort(arr,mid + 1 , right,target)
    return merge(arr , left_half , right_half ,target)
def merge( arr ,left , right,target):
    sizel = len(left)
    sizer = len(right)
    r = 0
    l = 0
    while l<sizel and r < sizer:
        if abs(arr[left[l]] - arr[right[r]]) > target:
            if arr[left[l]] > arr[right[r]]:
                r += 1
            else:
                l += 1
        else:
            break
            
    temp = []
    while l < sizel and r<sizer:
        if arr[left[l]] >=arr[right[r]]:
            temp.append(right[r])
            r += 1
        else:
            temp.append(left[l])
            l += 1
    while l < sizel:
        temp.append(left[l])
        l += 1
    while r < sizer:
        temp.append(right[r])
        r += 1
 
    return temp   

ans = mergeSort(arr , 0 , 2**n - 1,target)
ans.sort()
print(*[num +1 for num in ans])
