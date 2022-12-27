# Enter your code here. Read input from STDIN. Print output to STDOUT
a=int(input())
b=int(input())
m=int(input())
power=1
for i in range(b):
    power*=a
print(power)
print(power%m)
