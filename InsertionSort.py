#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort1(n, arr):
    # Write your code here
    for idx in range(n-1,-1,-1):
        temp = arr[idx]
        idx2 = idx-1
        while idx2>=0 and arr[idx2]>= temp:
            arr[idx2+1] = arr[idx2]
            print(*arr)
            idx2-=1
            
        arr[idx2+1]= temp
    print(*arr)     

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
