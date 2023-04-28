class Solution:
    def racecar(self, target: int) -> int:
        queue = deque([(1 , 0 , 0)])
        visited = set()
        position = 0
        
        
        while queue:
            speed , path , position = queue.popleft()
            if position == target:
                return path
            if (speed*2, position + speed) not in visited:
                queue.append((speed * 2 ,path + 1 , position + speed))
                visited.add((speed *2 , position + speed))
                
            if (-1 if speed > 0 else 1 , position) not in visited:
                if position + speed > target and speed > 0 or (position + speed < target and speed < 0):
                    queue.append(( -1 if speed > 0 else 1 , path + 1 , position))
                    visited.add((-1 if speed > 0 else 1 , position))
            
        return path