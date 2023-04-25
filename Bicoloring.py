import sys
from collections import defaultdict

def dfs(graph, visited, vertex, color):
    visited[vertex] = color
    for neighbor in graph[vertex]:
        if neighbor not in visited:
            if not dfs(graph, visited, neighbor, -color):
                return False
        elif visited[neighbor] == color:
            return False
    return True


n = int(input())
while n != 0:
    m = int(input())
    graph = defaultdict(set)
    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].add(b)
        graph[b].add(a)
    visited = {}
    for node in range(1, n+1):
        if node not in visited:
            if not dfs(graph, visited, node, 1):
                print("NOT BICOLOURABLE.")
                break
    else:
        print("BICOLOURABLE.")
    n = int(input())
