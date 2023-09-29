class TrieNode:
    def __init__(self):
        self.children = [None  for _ in range(26)]
        self.EOW = False

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
        node.EOW = True
    
    def search(self , word:str)->int:
        node = self.root
        ans = ""
        for l in word:
            index = ord(l) - ord('a')
            
            if node.children[index] and node.children[index].EOW:
                ans += l
                node = node.children[index]
            else:
                break
        return ans
            
        

class Solution:
    def longestWord(self, words: List[str]) -> str:
        trie = Trie()
        for word  in words:
            trie.addWord(word)
        ans = ""
        for word in words:
            temp = trie.search(word)
            if len(temp) > len(ans) or ( len(temp) == len(ans) and ans > temp ):
                ans = temp
        return ans
            