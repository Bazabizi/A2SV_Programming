class TreeNode:
    def __init__(self , val=""):
        self.right = None
        self.left = None
        self.val = val


class Trie:

    def __init__(self):
        self.tree = None

    def insert(self, word: str) -> None:
        root = self.tree
        if not root:
            self.tree = TreeNode(word)
            return

        parent = None
        while root:
            parent = root
            if root.val < word:
                root = root.right
            else:
                root = root.left
        
        if parent.val < word:
            parent.right = TreeNode(word)
        else:
            parent.left = TreeNode(word)
        
            
    def search(self, word: str) -> bool:
        
        root = self.tree
        while root:
            if root.val < word:
                root = root.right
            elif root.val > word:
                root = root.left
            else:
                return True
        
        return False

    def startsWith(self, prefix: str) -> bool:
        
        length = len(prefix)
        root = self.tree
        while root:
            if root.val[:length]> prefix:
                root = root.left
            elif root.val[:length ] < prefix:
                root = root.right
            else:
                return True
        return False
    


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)