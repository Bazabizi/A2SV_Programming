class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        deadends = set(deadends)
        visited = set()
        
        queue = deque([("0000" , 0)])
        if "0000" in deadends:
            return  - 1
        while queue:
            
            password , path = queue.popleft()
            if password == target:
                return path
            for idx in range(4):
                temp1 = ""
                temp2 = ""
                for i in range(4):
                    if i == idx:
                        temp1 += str(int(password[i]) + 1)[-1]
                        if password[i] == "0":
                            temp2 += "9"
                        else:
                            temp2 += str(int(password[i]) - 1)
                    else:
                        temp1 += password[i]
                        temp2 += password[i]
                
                if temp1 == target or temp2 == target:
                    return path + 1
                if temp1 not in visited and temp1 not in deadends:
                    queue.append((temp1 , path + 1))
                    visited.add(temp1)
                if temp2 not in visited and temp2 not in deadends:
                    queue.append((temp2 , path + 1))
                    visited.add(temp2)
                    
        
        return - 1