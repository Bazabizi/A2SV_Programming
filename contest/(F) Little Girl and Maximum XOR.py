minVal , maxVal = map(int,input().split())

if minVal == maxVal:
    print(0)
else:
    l = len(bin(minVal)) - 2
    r = len(bin(maxVal)) - 2
    ans = 0
    if r>l:
        ans = 2**(r ) -1
    else:
        idx = len(bin(maxVal)) - 2
        last = bin(maxVal)[2:]
        first = bin(minVal)[2:]
        i = 0
        while idx > 0 :
            if i >= len(first) or last[i] != first[i]:
                ans = (2**idx) - 1
                break
            idx -= 1
            i += 1
            
    print(ans)
