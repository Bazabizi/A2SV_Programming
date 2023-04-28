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
                if position + speed == target:
                    return path + 1
            if speed > 0 and (-1 , position) not in visited:
                queue.append(( -1 , path + 1 , position))
                visited.add((-1 , position))
            
            elif speed < 0 and (1 , position) not in visited:
                queue.append(( 1 , path + 1 , position))
                visited.add((1 , position))
            
            
            if position == target:
                return path
            
        return path