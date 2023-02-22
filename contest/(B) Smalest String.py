tests = int(input())
for _ in range(tests):
    n , m , k = map(int,input().split())
    first = 0
    second = 0
    ans = ""
    wordTemp1 = list(input())
    wordTemp2 = list(input())
    wordTemp1.sort()
    wordTemp2.sort()
    
    word1 = "".join(wordTemp1)
    word2 = "".join(wordTemp2)
    
    while word1 and word2:
        if word1 < word2 and first < k or second ==k:
            ans +=word1[0]
            second = 0
            word1 = word1[1:]
            first +=1
        else:
            ans += word2[0]
            first = 0
            word2 = word2[1:]
            second +=1
            
    print(ans)
