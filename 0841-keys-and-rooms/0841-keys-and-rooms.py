class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        locked = set([x for x in range(1 , len(rooms))])
        queue = deque([0])
        visited = set()
        while queue:
            room = queue.popleft()
            visited.add(room)
            # if room in locked:
            #     locked.remove(room)
            for keys in rooms[room]:
                if keys not in visited:
                    queue.append(keys)
        
        if len(visited) != len(rooms):
            return False
        
        return True