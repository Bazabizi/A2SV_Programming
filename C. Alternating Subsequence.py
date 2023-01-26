n = int(input())
 
for i in range(n):
    m = int(input())
    arr = list(map(int,input().split()))
    index = 0
    total = 0
    
    if arr[0] < 0:
        var = -10**9-1
        while index < m:
            while index < m and arr[index] <0:
                var = max( var, arr[index] )
                index += 1
            
            total += var
            var = 0
            
            while index < m and arr[index] > 0:
                var = max(var , arr[index])
                index +=1
                
            total += var
            var = -10**9-1
    else:                        
        var = 0
        while index < m:
            while index < m and arr[index] > 0:
                var = max( var, arr[index] )
                index += 1
            
            total += var
            var = -10**9 -1
            
            while index < m and arr[index] < 0:
                var = max(var , arr[index])
                index +=1
            if var != -10**9-1:
                total += var
                            
    print(total)
