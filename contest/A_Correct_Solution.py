num = list(input())
ans = input()
temp = ""
num.sort()
count = 0
for n in num:
    if n == "0":
        count += 1
# if count == len(num):
#     if
if count != 0 and count != len(num):
    temp += num[count]
    
for i in range(count):
    temp += "0"
if count == 0:
    count = -1
for n in num[count + 1:]:
    temp += n
if ans == temp:
    print("OK")
else:
    print("WRONG_ANSWER")