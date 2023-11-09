class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        
        meetings.sort()
        heap = []
        count = defaultdict(int)
        rheap = [i for i in range(n)]
        heapify(rheap) 
        for start , end in meetings:
            diff = end - start
            while heap and start >= heap[0][0]:
                heappush(rheap , heappop(heap)[1])
            
            if rheap:
                room = heappop(rheap)
                heappush(heap , (end , room))
                count[room] += 1  
                continue

            time , r = heappop(heap)
            count[r] += 1
            heappush(heap , (time + diff , r))
            
        value = max(count.values())
        cnt = 0
        ans = [0 ,0]

        for key , val in count.items():
            if ans[1] == val:
                ans = [min(ans[0] , key) , val]
            elif ans[1] < val:
                ans = [key , val]
        
        return ans[0]