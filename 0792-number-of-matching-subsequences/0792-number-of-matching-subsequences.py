# class TrieNode:
#     def __init__(self):
#         self.children = [None for _ in range(26)]
#         self.EOW = False
#         self.count = 0
# class Trie:
#     def __init__(self):
#         self.root = TireNode
        
#     def insert(self, word):
#         node = self.root
#         for l in word:
#             index = ord(l) - ord('a')
#             if not node.children[index][0]:
#                 node.children[index][0] = TrieNode()
#             node = node.children[index][0]
#         node.count += 1
#         node.EOW = True
    
#     def search(self , word):

        
class Solution:
    def binarySearch(self, prev , arr):
        left = -1
        right = len(arr)
        while left + 1 < right:
            mid = left + (right - left)//2
            if arr[mid] > prev:
                right = mid
            else:
                left = mid
        
        if right != len(arr):
            return arr[right]
        else:
            return -1
    
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        ans = 0
        index = defaultdict(list)
        
        for idx , l in enumerate(s):
            index[l].append(idx)
        
        for word in words:
            prev = self.binarySearch( -1 , index[word[0]] )
            if prev == -1:
                break
            for idx , l in enumerate(word[1:]):
                
                idx = self.binarySearch( prev , index[l])
                if idx == -1:
                    break
                prev = idx
            else:
                ans += 1
        
        return ans
        
            