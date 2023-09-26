class TrieNode:
    def __init__(self):
        self.children = [None for _ in range(26)]
        self.EOW = False

class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for l in word:
            index = ord(l) - ord('a')
            if not node.children[index]:
                node.children[index] = TrieNode()
            node = node.children[index]
    
        node.EOW = True
    

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        newTrie = Trie()
        for word in strs:
                newTrie.insert(word)
        ans = ""
        if "" in strs:
            return ""
        node = newTrie.root
        while node:
            count = 0
            index = 0
            for idx , child in enumerate(node.children):
                if child :
                    count += 1
                    index = idx
            if count == 1:
                ans += chr(index + ord('a'))
                node = node.children[index]
                if node.EOW:
                    break
            else:
                break
        
        return ans