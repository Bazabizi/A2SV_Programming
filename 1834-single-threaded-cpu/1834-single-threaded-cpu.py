class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        available = []
        process = []
        for idx , val in enumerate(tasks):
            tasks[idx].append(idx)
        heapify(tasks)
        ans = []
        ans.append(tasks[0][2])
        time = tasks[0][0]
        
        process = heappop(tasks)[1]
        while tasks:
            temp_time = process + time       
            
            while tasks and tasks[0][0] <= temp_time :
                enque  , ptime , idx =  heappop(tasks)
                heappush(available , (ptime , idx))
            if available:
                process ,idx = heappop(available)
                ans.append(idx)
                time = temp_time
            else:
                ans.append(tasks[0][2])
                time = tasks[0][0]
                process = heappop(tasks)[1]
                
            
        while available:
            ans.append(heappop(available)[1])
        return ans
        