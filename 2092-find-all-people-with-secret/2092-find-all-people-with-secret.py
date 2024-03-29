class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        parent = {i:i for i in range(n)}
        parent[firstPerson] = 0
        
        def find(child):
            while child != parent[child]:
                parent[child] = parent[parent[child]]
                child = parent[child]
            
            return child
        
        def union(x, y):
            repx = find(x)
            repy = find(y)
            
            if repx == 0 or repy == 0:
                parent[repx] = parent[repy] = 0 
            else:
                parent[repx] = repy
        
        meetings.sort(key = lambda x:x[-1])
        graph = defaultdict(list)
        for start , end  ,t in meetings:
            graph[t].append((start, end))
        
        ans = set([0 , firstPerson])
        length = len(meetings)
        
        for time , sameMeeting in graph.items():
        
            for x , y  in sameMeeting:
                union(x , y)
            for x , y in sameMeeting:
                rep = find(x)
                if rep != 0:
                    parent[x] = x
                    parent[y] = y
                else:
                    ans.add(x)
                    ans.add(y)
        ans = list(ans)
        return ans