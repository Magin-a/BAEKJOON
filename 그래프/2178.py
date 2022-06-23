#미로 탐색
#그래프 이론, 그래프 탐색
# 1은 이동가능 위치 0은 벽
import sys
from collections import deque
input = sys.stdin.readline
q = deque()
graph = []
move_x = [1, 0, -1, 0]
move_y = [0, 1, 0, -1]
cnt = 0
#입력부
n, m = map(int, input().split())
for _ in range(n):
    line = list(map(int, input().strip()))
    graph.append(line)

#bfs
q = deque()
q.append([0, 0]) # 시작점
while q:
    n_x, n_y = q.popleft()
    
    for i in range(4):
        next_x = n_x + move_x[i]
        next_y = n_y + move_y[i]
        
        if 0> next_x or next_x >= n or 0 >next_y or next_y >= m: 
            continue
        
        if graph[next_x][next_y]== 0:
            continue
        
        if graph[next_x][next_y]== 1:
            graph[next_x][next_y] = graph[n_x][n_y] +1
            q.append([next_x, next_y])

    
print(graph[n-1][m-1]) #도착지 수 출력
    
