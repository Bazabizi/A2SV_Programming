n = int(input())
for _ in range(n):
    test = int(input())
    words = []
    ans = ""
    check = set()
    for i in range(test):
        x = input()
        check.add(x)
        words.append(x)
    
    for word in words:
        found = False
        length = len(word)
        for idx in range(length):
            if word[:idx] in check and word[idx:] in check:
                ans+="1"
                break        
            
        else:
            ans += "0"
        
    print(ans)
