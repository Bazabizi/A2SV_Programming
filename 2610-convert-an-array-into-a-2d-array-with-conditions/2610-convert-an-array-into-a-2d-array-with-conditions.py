class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        store = defaultdict(int)
        for num in nums:
            store[num] += 1
        
        size = max(store.values())
        ans = [[] for _ in range(size)]
        
        for key , val in store.items():
            for i in range(val):
                ans[i].append(key)
        return ans