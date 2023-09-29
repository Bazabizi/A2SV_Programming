class TrieNode:
    def __init__(self):
        self.children = [None  for _ in range(26)]
        self.words = []
        self.EOW = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
        
    def addWord(self, word) -> None:
        node = self.root
        for l in word:
            index = ord(l) - ord('a')
            
            if not node.children[index]:
                node.children[index] = TrieNode()
            
            node = node.children[index]
            if len(node.words) < 3:
                node.words.append(word)
            
        node.EOW = True
    
    def search(self,word):
        node = self.root
        ans = []
        for l in word:
            temp  = []
            index = ord(l) - ord('a')
            if node.children[index]:
                temp.extend(node.children[index].words)
                
            else:
                node.children[index] = TrieNode()
            node = node.children[index]
            ans.append(temp)
        return ans

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        trie = Trie()
        products.sort()
        for word in products:
            trie.addWord(word)
        
        ans = trie.search(searchWord)
        return ans