#DFS와 BFS
import sys
from collections import deque
input = sys.stdin.readline

zum, cnt, start = map(int, input().split())

q = deque()
graph = [[] for _ in range(zum+1)]
visited = []

for _ in range(cnt):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

def dfs(start, graph, visited):
    visited.append(start)
    for i in graph[start]:
        if i not in visited:
            dfs(i, graph, visited)

def bfs(start, graph, visited, q):
    q.append(start)
    visited.append(start)

    while q:
        test = q.popleft()
        for i in graph[test]:
            if i not in visited:
                q.append(i)
                visited.append(i)


dfs(start, graph, visited)
for i in visited:
    print(i, end=' ')
visited = []
print()
bfs(start, graph, visited, q)
for i in visited:
    print(i, end=' ')
