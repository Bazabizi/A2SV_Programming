if __name__ == '__main__':
    N = int(input())
    ans=[]
    
    for num in range(N):
        enter = input().split()
        if enter[0] =="insert":
            ans.insert(int(enter[1]),int(enter[2]))
            
        elif enter[0] =="print":
            print(ans)
        
        elif enter[0]=="remove":
            ans.remove(int(enter[1]))
        
        elif enter[0] =="append":
            ans.append(int(enter[1]))
        elif enter[0]=="sort":
            ans.sort()
        elif enter[0]=="pop":
            ans.pop()
        elif enter[0]=="reverse":
            ans.reverse()
        
            
