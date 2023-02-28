class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        queue = deque(tickets)
        time = 0
        size = len(tickets)
        while True:
            if queue[0] > 0:
                queue[0] -= 1
                time += 1
            if queue[k] == 0:
                break
            queue.append(queue[0])
            queue.popleft()
            k = (k-1) % size
        
        return time