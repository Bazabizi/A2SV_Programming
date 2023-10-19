class TrieNode:
    def __init__(self):
        self.children = {}
        self.eow = False
class Trie:
    def __init__(self):
        self.root = TrieNode()
    def insert(self, word: str) -> None:
        node = self.root
        for ch in word:
            indx = ord(ch) - 97
            if indx not in node.children:
                node.children[indx] = TrieNode()
            node = node.children[indx]
        node.eow = True
    @lru_cache
    def search(self,ind,word,count):
        node = self.root
        if count > 1 and ind >= len(word):
            return True
        for i in range(ind,len(word)):
            ch = word[i]
            indx = ord(ch) - 97
            if indx in node.children:
                node = node.children[indx]
            else:
                return False
            if node.eow:
                if self.search(i+1,word,count+1):
                    return True
        return False     
class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        words.sort(key = lambda x :len(x))
        trie = Trie()
        for x in words:
            trie.insert(x)
        ans = []
        for x in words:
            if len(x) < 2:
                continue
            val = trie.search(0,x,0)
            if val:
                ans.append(x)
        return ans