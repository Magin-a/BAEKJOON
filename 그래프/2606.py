#바이러스
import sys
input = sys.stdin.readline

cnt = int(input())
graph = [[] for _ in range(cnt+1)]
visited = []



test = int(input())
for _ in range(test):
    index, link = map(int, input().split())
    graph[index].append(link)
    graph[link].append(index)

print(graph)
def dfs(start, graph, visited):
    for i in graph[start]:
        if i not in visited:
            visited.append(i)
            dfs(i, graph, visited)


dfs(1, graph, visited)
print(len(visited)-1)
