class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        visited = defaultdict(int)
        
        for search in cpdomains:
            num , site = search.split()
            temp = site.split(".")
            cur = temp[-1]
            visited[cur]+= int(num)
            
            for idx in range(len(temp)-1,0,-1):
                pre = idx-1
                cur = temp[pre] + '.' + cur
                visited[cur]+= int(num)
        
        ans=[]
        
        for key in visited:
            temp = str(visited[key]) + " " + key 
            ans.append(temp)
        
        return ans
                
                
                
            