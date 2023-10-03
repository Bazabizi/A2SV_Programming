class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        store = set()
        count = defaultdict(int)
        for id , time in logs:
            if (id , time) in store:
                continue
            store.add((id , time))
            count[id] += 1
        ans = [0]*k
        for key , val in count.items():
            ans[val - 1] += 1
        return ans