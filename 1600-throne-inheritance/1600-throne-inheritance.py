class ThroneInheritance:

    def __init__(self, kingName: str):
        
        self.dead = set()
        self.kingdom = defaultdict(list)
        self.kingdom[kingName] = []
    def birth(self, parentName: str, childName: str) -> None:
        self.kingdom[parentName].append(childName)

    def death(self, name: str) -> None:
        self.dead.add(name)
        
    def getInheritanceOrder(self) -> List[str]:
        self.inheritance = []
        visited = set()
        for val in self.kingdom:
            if val not in visited:
                self.dfs(val , visited)
        
        return self.inheritance
        
    def dfs(self,king , visited):
        visited.add(king)
        if king not in self.dead:
            self.inheritance.append(king)
        
        if king in self.kingdom:
            for child in self.kingdom[king]:
                if child not in visited :
                    self.dfs(child , visited)
            
        
        
# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance(kingName)
# obj.birth(parentName,childName)
# obj.death(name)
# param_3 = obj.getInheritanceOrder()