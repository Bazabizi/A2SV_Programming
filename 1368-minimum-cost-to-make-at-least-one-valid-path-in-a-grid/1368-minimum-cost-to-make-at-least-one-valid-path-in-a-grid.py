class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        direction = [(0 , 1),(0 , -1),(1 , 0),(-1, 0)]
        graph = defaultdict(list)
        rowlength = len(grid)
        colLength = len(grid[0])
        def inbound(row , col):
            return 0 <= row < len(grid) and 0 <= col < len(grid[0])
        
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                
                if grid[row][col] != 1 and inbound(row , col + 1):
                    graph[(row, col)].append((1 , (row , col + 1)))
                else:
                    graph[(row, col)].append((0 , (row , col + 1)))

                if grid[row][col] != 2 and inbound(row , col - 1):
                    graph[(row, col)].append((1 , (row , col - 1)))
                else:
                    graph[(row, col)].append((0 , (row , col - 1)))
        
                if grid[row][col] != 3 and inbound(row + 1 , col ):
                    graph[(row, col)].append((1 , (row + 1, col)))
                else:
                    graph[(row, col)].append((0 , (row + 1, col )))
        
                if grid[row][col] != 4 and inbound(row - 1 , col):
                    graph[(row, col)].append((1 , (row - 1 , col)))
                else:
                    graph[(row, col)].append((0 , (row - 1, col )))
        
        distances = defaultdict(lambda:float('inf'))
        distances[(0 , 0)] = 0
        visited =set()
        heap = [(0 , ( 0 , 0))]
        while heap:
            distance , cord = heappop(heap)
            if cord in visited:
                continue
            visited.add(cord)
            
            for dis , end in graph[cord]:
                if dis + distance < distances[end]:
                    distances[end] = dis + distance
                    heappush(heap , (distances[end] , end))
       
        return distances[(rowlength -1 , colLength - 1)]