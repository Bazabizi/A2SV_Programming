# Enter your code here. Read input from STDIN. Print output to STDOUT
size1=input()
setA=set(map(int ,input().split()))
size2=input()
setB=set(map(int ,input().split()))

setC=set(setA.difference(setB))
print(len(setC))
