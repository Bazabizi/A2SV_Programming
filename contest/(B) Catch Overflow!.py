from collections import defaultdict
from collections import Counter
n = int(input())
stack = []
ans = 0

for _ in range(n):
    word = input()
    if word[0] == "f":
        num = int(word[4:])
        if not stack:
            stack.append( num )
        else:
            x = stack[-1]* num
            if x > 2**32 -1:
                stack.append(float("inf"))
            else:
                stack.append(stack[-1] * num)
    
    elif word =="end":
        stack.pop()
    elif word == "add":
        if stack:
            if stack[-1]==float("inf"):
                print("OVERFLOW!!!")
                break
            ans += stack[-1]
        else:
            ans += 1
    if ans > 2**32 -1:
        print("OVERFLOW!!!")
        break
else:
    print(ans)
    
