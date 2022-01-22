#바이러스
import sys
input = sys.stdin.readline

cnt = int(input())
graph = [[] for _ in range(cnt)]

test = int(input())
for _ in range(test):
    index, link = map(int, input().split())
    graph[index-1].append(link-1)
    graph[link-1].append(index-1)

print(graph)
