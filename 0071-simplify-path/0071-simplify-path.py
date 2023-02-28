class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
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
    
