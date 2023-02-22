n = int(input())
 
for _ in range(n):
    row1 = list(map(int,input().split()))
    row2 = list(map(int,input().split()))
    ans = row1 + row2
    matrix = []
    matrix.append(row1)
    matrix.append(row2)
    ans.sort()
    
    if matrix[1][1]==ans[-1] and matrix[0][0]==ans[0]:
        print("YES")
    elif matrix[0][1]==ans[-1] and matrix[1][0]==ans[0]:
        print("YES")
    elif matrix[1][1]==ans[0] and matrix[0][0]==ans[-1]:
        print("YES")
    elif matrix[0][1]==ans[0] and matrix[1][0]==ans[-1]:
        print("YES")
    else:
        print("NO")
