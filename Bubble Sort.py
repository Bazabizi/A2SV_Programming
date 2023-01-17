#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countSwaps' function below.
#
# The function accepts INTEGER_ARRAY a as parameter.
#

def countSwaps(a):
    # Write your code here
    swap =0
    size = len(a)
    for idx in range(size):
        for idx2 in range(size-idx-1):
            if a[idx2] > a[idx2+1]:
                a[idx2] , a[idx2+1] = a[idx2+1] , a[idx2]
                swap+=1
    
    print("Array is sorted in",swap,"swaps.")
    print("First Element:",a[0])
    print("Last Element:",a[-1])
    
if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    countSwaps(a)
