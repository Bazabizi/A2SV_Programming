a , b, ab = map(int ,input().split())
count_a = a + ab
count_b = b + ab
 
if count_a == count_b:
    print(2*count_a)
elif count_a < count_b :
    print(1+ 2*count_a)
else:
    print(2*count_b +1)
