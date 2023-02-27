class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        position_time = []
        stack = []
        size = len(speed)
        for idx in range(size):
            remaining_distance = target - position[idx] 
            timeTaken =( remaining_distance / speed[idx] )
            position_time.append( ( remaining_distance , timeTaken ) )
        
        position_time.sort()
        
        for pos , time in position_time:
            if not stack or stack[-1] < time:
                stack.append(time)
        
        return len(stack)