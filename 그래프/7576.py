import sys
from collections import deque
input = sys.stdin.readline

m, n = map(int ,input().split())

graph = []
q = deque()
visited = []
cnt = 0
#1은 익은 토마토, 정수 0은 익지 않은 토마토, 정수 -1은 토마토가 들어있지 않은 칸
for a in range(n):
    graph.append(list(map(int, input().split())))

    for b in range(m): #익은 토마토 큐에 저장
        if graph[a][b]==1:
            q.append([a,b])

move_x = [-1, 1, 0, 0]
move_y = [0, 0, -1, 1]

def bfs():
    while q:
        test_x, test_y = q.popleft()

        for num in range(4):
            see_x = test_x + move_x[num]
            see_y = test_y + move_y[num]

            if 0 <= see_x < n and 0 <= see_y < m and graph[see_x][see_y] == 0:
                q.append([see_x,see_y])
                graph[see_x][see_y] = graph[test_x][test_y]+1
            

bfs()
cnt = 0
for i in graph:
    for j in i:
        if j==0:
            print(-1)
            exit(0)
    cnt = max(cnt,max(i))
print(cnt-1)
