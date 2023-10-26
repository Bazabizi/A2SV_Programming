class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        count = Counter(arr)
        # count = {}
        arr.sort()
        N = 10**9 + 7
        for m in arr:
            count[m] = 1     
            for n in arr:
                if m % n == 0 and m // n in count:
                    count[m] += count[n] * count[m//n]
        
        ans = sum(count.values()) % N
        return ans