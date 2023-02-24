n= int(input())
 
for i in range (n):
    ans =[]
    t = input()
    for j in range(8):
        z=input()
        ans.append(z)
    a = 0
    b = 0
    check = True
    check2 = True
    for row in range(7):
        for col in range(7):
            if ans[row][col] =="#":
                if check:
                    if ans[row+1][col-1] =="#" and row+1 < 8 and col-1 >-1 :
                        a = col + row
                        check = False
                        
                if check2:
                    if ans[row+1][col+1]=="#" and row+1 < 8 and col+1 <8:
                        b = row - col
                        check2 = False
        #print(a)
    x = (a-b)//2 
    y = (b+a)//2
    print(y+1,x+1)
