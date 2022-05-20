import sys
from collections import deque
input = sys.stdin.readline

m, n = map(int ,input().split())

graph = []
q = deque()
visited = []
#1은 익은 토마토, 정수 0은 익지 않은 토마토, 정수 -1은 토마토가 들어있지 않은 칸
for _ in range(n):
    graph.append(list(map(int, input().split())))

move_x = [-1, 1, 0, 0]
move_y = [0, 0, -1, 1]

def bfs(x, y, cnt):
    q.append([x, y])
    visited.append([x, y])
    
    while q:
        test_x, test_y = q.popleft()
        cnt +=1
        for num in range(4):
            see_x = test_x + move_x[num]
            see_y = test_y + move_y[num]

            if not(0 <= see_x < n) or not( 0 <= see_y < m):
                continue
            
            if graph[see_x][see_y] !=0 or [see_x, see_y] in visited:
                continue

            
            graph[see_x][see_y] = 1
            q.append([see_x, see_y])
            

    print(cnt)





for a in range(n):
    for b in range(m):
        if graph[a][b] == 1 :
            bfs(a, b, 0)

