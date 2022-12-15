#주차시스템
import sys
from collections import deque
input = sys.stdin.readline

n , m = map(int, input().split()) #row, col
g = []
move_x =[-1, 0, 1, 0]
move_y = [0, -1, 0, 1]
q = deque()
result =0

for _ in range(n):
    line = list(map(int, input().split()))
    g.append(line)


def bfs(y, x, cnt):
    global result
    q.append([y,x])
    
    while q:
        a_y, a_x = q.popleft()
        if g[a_y][a_x] == 0:
            cnt += 1
            g[a_y][a_x] = 1

        if g[a_y][a_x] == 2:
            cnt -= 2
            g[a_y][a_x] = 1

        for i in range(4):
            t_x = a_x + move_x[i]
            t_y = a_y + move_y[i]

            if 0 > t_x or t_x >= m or 0 > t_y or t_y >= n or g[t_y][t_x] == 1:
                continue

            q.append([t_y, t_x])
    result = max(result, cnt)

for a in range(n):
    for b in range(m):
        if g[a][b] != 1:
            cnt = 0
            bfs(a,b, cnt)
print(result)