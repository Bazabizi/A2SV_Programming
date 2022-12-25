class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        for idx , word in enumerate(words[1:]):
            if not self.compare_order(words[idx] , word , order):
                return False
        return True


    def compare_order(self ,word1 , word2 , order):
        length = min(len(word1) , len(word2))

        for idx in range(length):
            if order.index(word1[idx]) > order.index(word2[idx]):
                return False
            if order.index(word1[idx]) < order.index(word2[idx]):
                return True

        if len(word1)<=len(word2):
            return True
        else:
            return False 

        return True
