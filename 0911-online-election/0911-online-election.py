class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        self.votes = persons
        self.time = times
        count = defaultdict(list)
        count[persons[0]] = [1 , 0]
        maxVal = persons[0]
        self.maxValue = [persons[0]]
        for idx , val in enumerate(persons[1:]):
            if val not in count:
                count[val] =[1,idx]
            else:
                count[val][0] += 1
                count[val][1] = idx
            if count[val][0] >= count[maxVal][0]:
                maxVal = val
            self.maxValue.append(maxVal)   
        
    def q(self, t: int) -> int:
        left  = -1
        right = len(self.time)
        mid = -1
        find = False
        
        while left + 1 < right:
            mid = left + (right - left) // 2
            if self.time[mid] > t:
                right = mid
                
            elif self.time[mid] < t:
                left = mid
            else:
                
                return self.maxValue[mid]
        
        return self.maxValue[right - 1]
                