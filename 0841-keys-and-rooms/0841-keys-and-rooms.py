class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        queue = deque([0])
        visited = set()
        while queue:
            room = queue.popleft()
            visited.add(room)
            for keys in rooms[room]:
                if keys not in visited:
                    queue.append(keys)
        
        if len(visited) != len(rooms):
            return False
        
        return True