#미로 탐색
#그래프 이론, 그래프 탐색
# 1은 이동가능 위치 0은 벽
import sys
from collections import deque
input = sys.stdin.readline
q = deque()
graph = []
move_x = [1, 0]
move_y = [0, 1]
cnt = 0

n, m = map(int, input().split())
for _ in range(n):
    line = list(map(int, input().strip()))
    graph.append(line)

q = deque([0, 0])
fin_x, fin_y = n-1, m-1

while q:
    n_x, n_y = q.popleft()
    cnt += 1
    compare = []
    for i in range(2):
        next_x = n_x + move_x[i]
        next_y = n_y + move_y[i]

        if 0> next_x or next_x >= m or 0 >next_y or next_y >= n or graph[next_x][next_y]==0: 
            continue

