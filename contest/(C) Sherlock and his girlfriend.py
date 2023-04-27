n = int(input())
is_prime = [1 for x in range( n + 2)]
ans = []
is_prime[1],is_prime[0] = 0 , 0
i = 2
while i * i <= n + 1:
       if is_prime[i]:
           j = i * i
           while j <= n + 1:
               is_prime[j] = 0
               j += i
       i += 1
prime = False
composite = False
for val in is_prime[2:]:
    if val == 1:
        ans.append(1)
        prime = True
    else:
        ans.append(2)
        composite = True
if prime and composite:
    print(2)
else:
    print(1)

print(*ans)
