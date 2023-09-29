class TrieNode:
    def __init__(self):
        self.children = [[None , 0] for _ in range(26)]
        self.EOW = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
        self.find = defaultdict(int)

    def addWord(self, word: str , value:int) -> None:
        node = self.root
        val = value
        if word in self.find:
            val = value - self.find[word]
        self.find[word] = value
        for l in word:
            index = ord(l) - ord('a')
            
            if not node.children[index][0]:
                node.children[index] = [TrieNode() , val]
            else:
                node.children[index][1] += val
            node = node.children[index][0]
        node.EOW = True

        
    def search(self, word: str) -> int:
        node = self.root
        ans = 0
        for l in word:
            index = ord(l) - ord('a')
            if not node.children[index][0]:
                ans = 0
                break
            ans = node.children[index][1]
            node = node.children[index][0]
        
        return ans
            
        

class MapSum:

    def __init__(self):
        self.trie = Trie()
        
    def insert(self, key: str, val: int) -> None:
        self.trie.addWord(key ,val)

    def sum(self, prefix: str) -> int:
        return self.trie.search(prefix)


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)