num = input()
ans = ""
if num[0] =="9" or num[0] < "5":
    ans += num[0]
else:
    ans += str( 9 - int(num[0]))
for l in num[1:]:
    if int(l) >= 5 :
        ans += str(9- int(l))
    else:
        ans += l
print(ans)
