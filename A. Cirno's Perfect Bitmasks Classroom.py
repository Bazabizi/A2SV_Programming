from collections import defaultdict
from collections import Counter
n = int(input())
for _ in range(n):
    x = 0
    num = int(input())
    val = 1
    count = bin(num).count("1")
    if count > 1:
        while True:
            if num & val:
                x |= val
                break
            val <<= 1
    else:
        while True:
            if not(num & val):
                x |= val
                break
            val <<= 1
        x = x | num
    print(x)
