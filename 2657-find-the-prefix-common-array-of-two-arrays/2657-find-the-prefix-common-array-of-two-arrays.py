class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        ans = []
        length = len(A)
        store = defaultdict(int)
        count = 0
        for idx in range(length):
            if A[idx] in store:
                count += 1
            store[A[idx]] += 1  
            if B[idx] in store:
                count += 1          
            store[B[idx]] += 1
            ans.append(count)
        return ans