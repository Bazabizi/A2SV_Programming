n =int(input())
list1=[]
for i in range(200):
    list1.append(str(i))
 
for i in range(n):
    sent=[None]*200
    word=input().split()
    for letter in word:
        ans=""
        for idx in range(len(letter)):
            if letter[idx] in list1:
                index=int(letter[idx])
            else:
                ans +=letter[idx]
        sent[index]= ans
        news=""
    for val in sent:
        
        if val!=None:
            news +=val+" "
            #print(val,end=" ")
    news=news[:-1]
    print(news)
