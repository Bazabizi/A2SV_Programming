class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        filePath= defaultdict(list)
        
        for path in paths:
            
            file = path.split()
            size = len(file)
            
            for idx in range(1,size):
                first = file[idx].index("(")
                last = file[idx].index(")")
                
                directory =file[0] +"/" +file[idx][:first]
                content = file[idx][first+1:last]
                
                filePath[content].append(directory)
        
        ans=[]
        for value in filePath.values():
            
            if len(value) > 1:
                ans.append(value)
        return ans