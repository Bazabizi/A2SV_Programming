class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        starts = []
        ends = []
        for start , end in flowers:
            starts.append(start)
            ends.append(end + 1)
        
        starts.sort()
        ends.sort()
        ans = []
        for p in people:
            left = bisect_right(starts , p)
            right = bisect_right(ends , p)
            ans.append(left - right)
        
        return ans