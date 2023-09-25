class Solution:
    def minimumTotalPrice(self, n: int, edges: List[List[int]], price: List[int], trips: List[List[int]]) -> int:
        mem = defaultdict(int)
        graph = defaultdict(list)
        freq  = defaultdict(int)
        for start , end in edges:
            graph[start].append(end)
            graph[end].append(start)
        
        def dfs(vertix , end):
            
            if vertix == end:
                return True
            
            for val in graph[vertix]:
                if val not in visited:
                    visited.add(val)
                    if dfs(val , end):
                      
                        freq[val] += 1
                        return True
            return False
        
        def dp(vertix , color , parent):
            ans = price[vertix]*freq[vertix]
            if color == 1:
                ans //= 2
            if (vertix , color) in mem:
                return mem[(vertix, color)]
            if len(graph[vertix]) == 1 and parent != -1:
                
                mem[(vertix , color)] = ans
                return mem[(vertix , color)]
            if color == 1:
                for val in graph[vertix]:
                    
                    if val!= parent:
                        ans += dp(val , -1 , vertix)
                
            else:
                for val in graph[vertix]:
                    if val != parent:
                        ans += min(dp(val , 1 , vertix) , dp(val , -1 , vertix))
            mem[(vertix , color)] = ans
            return ans
        
        
        for trip in trips:
            freq[trip[0]] += 1
            
            visited = set([trip[0]])
            dfs(trip[0] , trip[1])
        # print(freq)
        
        
        ans = min(dp(0 , 1 , -1) , dp(0 , -1 , -1))
        
        return ans
                    
                    
                    
                    
                    
                    
                    