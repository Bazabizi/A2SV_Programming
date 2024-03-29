from typing import List

from collections import deque , defaultdict
from typing import List


class Solution:
    def minimumTime(self, n : int,m : int, edges : List[List[int]]) -> int:
        # code here
        ans = [1]*n
        graph = defaultdict(list)
        indegree = defaultdict(int)
        for start , end in edges:
            graph[start].append(end)
            indegree[end] += 1
        
        queue = deque()

        for i in range(1 , n+ 1):
            if i not in indegree:
                queue.append(i)
        time = 1
        while queue:
            size = len(queue)
            
            for _ in range(size):
                vertix = queue.popleft()
                ans[vertix - 1] = str(time)
                for val in graph[vertix]:
                    indegree[val] -= 1
                    if indegree[val] == 0:
                        queue.append(val)
            time += 1
        
        return " ".join(ans)
#{ 
 # Driver Code Starts
class IntArray:
    def __init__(self) -> None:
        pass
    def Input(self,n):
        arr=[int(i) for i in input().strip().split()]#array input
        return arr
    def Print(self,arr):
        for i in arr:
            print(i,end=" ")
        print()



class IntMatrix:
    def __init__(self) -> None:
        pass
    def Input(self,n,m):
        matrix=[]
        #matrix input
        for _ in range(n):
            matrix.append([int(i) for i in input().strip().split()])
        return matrix
    def Print(self,arr):
        for i in arr:
            for j in i:
                print(j,end=" ")
            print()


if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        a=IntArray().Input(2)
        
        
        edges=IntMatrix().Input(a[1], a[1])
        
        obj = Solution()
        res = obj.minimumTime(a[0],a[1], edges)
        
        print(res)
        

# } Driver Code Ends