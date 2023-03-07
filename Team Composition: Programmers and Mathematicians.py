test_cases = int(input())

for _ in range(test_cases):
    prog , math = map(int,input().split())
    ans = min(prog,math , (prog + math)//4)
    
    print(ans)
