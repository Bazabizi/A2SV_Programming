class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        length = len(path)
        idx = 0
        for file in path.split("/"):
            
            if file =="..":
                if stack:
                    stack.pop()
            else:
                if file != "." and file != "":
                    stack.append(file)
        ans ="/".join(stack)
        ans ="/" + ans
        return ans
    
