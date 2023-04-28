board = int(input())
qrow , qcol = map(int,input().split())
krow , kcol = map(int,input().split())
trow , tcol = map(int,input().split())
if qrow > krow and trow < qrow and qcol > kcol and qcol > tcol or (qrow < krow and trow > qrow and qcol <= kcol and qcol < tcol):
    print("YES")
elif qrow > krow and trow < qrow and qcol < kcol and qcol < tcol or (qrow < krow and qrow < trow  and qcol > kcol and qcol > tcol):

    print("YES")
else:
    print("NO")
   
