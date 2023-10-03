class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        store = defaultdict(list)
        ans = []
        for idx , num in enumerate(groupSizes):
            store[num].append(idx)
        
        for key , val in store.items():
            count = 0
            temp = []
            for v in val:
                temp.append(v)
                count += 1
                if count == key:
                    count = 0
                    ans.append(temp)
                    temp = []
            if temp:
                ans.append(temp)
        
        return ans