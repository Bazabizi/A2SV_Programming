class TrieNode:
    def __init__(self):
        self.children = [None for _ in range(26)]
        self.EOW = False
        self.count = 0

class Trie:
    def __init__(self):
        self.root = TrieNode()
        
    def addWord(self, word: str ) -> None:
        node = self.root
        for l in word:
            index = ord(l) - ord('a')
            
            if not node.children[index]:
                node.children[index] = TrieNode()
            
            
            node = node.children[index]
            node.count += 1
        node.EOW = True
        
    def search(self, word):
        node = self.root
        ans = 0
        for l in word:
            index = ord(l) - ord('a')
            node = node.children[index]
            ans += node.count
            
        return ans
        
class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        trie = Trie()
        for word in words:
            trie.addWord(word)
        
        ans = []
        for word in words:
            val = trie.search(word)
            ans.append(val)
        
        return ans
        