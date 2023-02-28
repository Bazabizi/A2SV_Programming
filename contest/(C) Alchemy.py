from collections import defaultdict
size = int(input())
ingred = list(map(int,input().split()))
edward =  0 
alph = 0

ansEd = 0
ansAlp = 0
left = 0
right = len(ingred) - 1
leftSum = 0
rightSum = 0
# right -= 1
# left += 1
while right > left:
    if leftSum < rightSum:
        leftSum += ingred[left]
        left += 1
        ansEd += 1
    if leftSum > rightSum and right > left:
        rightSum += ingred[right]
        right -= 1
        ansAlp += 1 
    if leftSum == rightSum and right > left:
        leftSum += ingred[left]
        rightSum += ingred[right]
        ansAlp += 1
        ansEd += 1
        left += 1
        right -= 1
    if right == left:
        if leftSum > rightSum:
            ansAlp += 1
            right -= 1
            break
        else:
            ansEd += 1
            left += 1
            break
if right == left:
    if leftSum > rightSum:
        ansAlp += 1
    else:
        ansEd += 1
            
print(ansEd,ansAlp)
