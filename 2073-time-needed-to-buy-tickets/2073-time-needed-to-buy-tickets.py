class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        queue = deque(tickets)
        minVal = queue[k]
        time = 0
        idx = 0
        size = len(tickets)
        while idx < size:
            if idx <= k:
                time += min(queue[0],minVal)
            else:
                if queue[0] >=minVal:
                    time += minVal -1
                else:
                    time += queue[0]
            queue.popleft()
            idx += 1
        return time