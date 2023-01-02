n=int(input())
word1=input()
size = len(word1)
temp=[]
for idx in range(size):
    temp.append(word1[idx])
 
for i in range(n-1):
    wordtemp = input()
    
    for idx in range(size):
        if wordtemp[idx] != "?":
            if temp[idx]!= "?" and wordtemp[idx]!= temp[idx]:
                temp[idx]=1
            else:
                temp[idx]=wordtemp[idx]
 
ans=""
 
for i in range(size):
    if temp[i]=="?":
        temp[i] = "a"
        
    elif temp[i] == 1:
        temp[i] ="?"
        
    ans+= temp[i]
 
print(ans)
