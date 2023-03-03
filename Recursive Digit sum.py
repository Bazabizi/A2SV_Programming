#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'superDigit' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING n
#  2. INTEGER k
#
def answer(s):
    if len(s) == 1:
        return int(s[0])
    ans = 0
    for num in s:
        ans += int(num)
    return answer(str(ans))
        
def superDigit(n, k):
    # Write your code here
    sumUp = 0
    for num in n:
        sumUp += int(num)
    sumUp *= k
    sumUp = str(sumUp)
    return answer(sumUp)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = first_multiple_input[0]

    k = int(first_multiple_input[1])

    result = superDigit(n, k)

    fptr.write(str(result) + '\n')

    fptr.close()
