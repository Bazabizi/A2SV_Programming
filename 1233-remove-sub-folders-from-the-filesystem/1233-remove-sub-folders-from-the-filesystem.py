class TrieNode:
    def __init__(self):
        self.children = {}
        self.EOW = False
        self.count = 0
        self.Word = ""

class Trie:
    def __init__(self):
        self.root = TrieNode()
        
    def addWord(self, word: str  , ans:str) -> None:
        node = self.root
        for l in word:
                
            if  l not in node.children :
                node.children[l] = TrieNode()
            
            
            node = node.children[l]
            node.count += 1
        node.EOW = True
        node.Word = ans
    def search(self) -> List[str]:
        node = deque([self.root])
        ans = []
        while node :
            newNode = node.popleft()
            
            if newNode.EOW:
                ans.append(newNode.Word)
                continue
                
            for child in newNode.children:
                node.append(newNode.children[child])

        return ans
class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        trie = Trie()
        for word in folder:
            newWord = word.split('/')
            trie.addWord(newWord , word)
        
        ans = trie.search()
        return ans
        
        