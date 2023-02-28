class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        queue = deque(tickets)
        minVal = queue[k]
        time = 0
        idx = 0
        size = len(tickets)
        while idx < size:
            # print(queue)
            if idx <= k:
                time += min(queue[0],minVal)
            else:
                time += min(queue[0],minVal-1) 
                
            queue.popleft()
            idx += 1
        return time