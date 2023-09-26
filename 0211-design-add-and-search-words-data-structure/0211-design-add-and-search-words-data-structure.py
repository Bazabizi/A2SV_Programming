class TrieNode:
    def __init__(self):
        self.children = [None for _ in range(26)]
        self.EOW = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root
        for l in word:
            index = ord(l) - ord('a')
            if not node.children[index]:
                node.children[index] = TrieNode()
            node = node.children[index]
        node.EOW = True

        
    def search(self, word: str) -> bool:
        node = deque()
        node.append(self.root)
        for l in word:
            index = ord(l) - ord('a')
            
            size = len(node)
            for idx in range(size):
                newNode = node.popleft()
                if l != '.':
                    if not newNode.children[index]:
                        continue
                    node.append(newNode.children[index])
                else:
                    for child in newNode.children:
                        if child:
                            node.append(child)
            if not node:
                return False

        for newNode in node:
            if newNode.EOW:
                return True
        return False
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)