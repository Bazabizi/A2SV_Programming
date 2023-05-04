class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        count = defaultdict(int)
        for word in words:
            count[word] += 1
        heap = []
        size = 0
        for key , value in count.items():
            heappush(heap ,(-value , key))
        ans = []
        while size < k:
            ans.append(heappop(heap)[1])
            size += 1
        return ans