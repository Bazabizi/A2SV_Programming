class TrieNode:
    def __init__(self):
        self.children = {}
        self.EOW = False
        self.index = 0
class Trie:
    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word , idx):
        node = self.root
        for l in word:
            if l not in node.children:
                node.children[l] = TrieNode()
            
            node = node.children[l]
            node.index = idx
        node.EOW = True
    
    def search(self , word):
        node = self.root
        for l in word:
            if l not in node.children:
                return -1
            node = node.children[l]
        
        return node.index
        
    def traverse(self, node):
        ans = -1

        if node.EOW:
            ans = max(ans, node.index)


        for child in node.children:
            ans = max(ans, self.traverse(node.children[child]))

        return ans
    
class WordFilter:

    def __init__(self, words: List[str]):
        self.trie = Trie()
        
        for index , word in enumerate(words):
            for idx , l in enumerate(word):
                val = word[idx:] + '{' + word
                self.trie.insert(val , index)

    def f(self, pref: str, suff: str) -> int:
        word = suff+ '{'+ pref
        
        return self.trie.search(word)


# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(pref,suff)