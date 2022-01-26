#적록색약
import sys
input = sys.stdin.readline

N = int(input())
result, result2 = 0, 0

graph = [list(input().rstrip()) for _ in range(N)]
visited = [[False]*N for _ in range(N)]

trans_x = [1, 0, -1, 0]
trans_y = [0, -1, 0, 1]

def dfs(x, y):
    c_color = graph[x][y]
    visited[x][y] = True
    
    for a in range(4):
        t_x = x + trans_x[a]
        t_y = y + trans_y[a]
        if (0 <= t_x < N) and (0 <= t_y <N):
            if visited[t_x][t_y] == False:
                if graph[t_x][t_y] == c_color:
                    dfs(t_x, t_y)

def bfs(x, y):
    q.append([x, y])
    visited[x][y] = 1

    while q:
        x,y = q.popleft()
        for a in range(4):
            t_x = x + trans_x[a]
            t_y = y + trans_y[a]
            if not((0 <= t_x < N) and (0 <= t_y <N)):
                continue
            if graph[t_x][t_y] != graph[x][y] or visited[t_x][t_y] == 1:
                continue
            visited[t_x][t_y] = 1
            q.append([t_x, t_y]) 

                    
                    

for i in range(N):
    for j in range(N):
        if visited[i][j] == False:
            dfs(i,j)
            result += 1

# R -> G 변환
for i in range(N):
    for j in range(N):
        if graph[i][j] == "R":
            graph[i][j] = "G"

#탐색 초기화
visited = [[False]*N for _ in range(N)] 
for i in range(N):
    for j in range(N):
        if visited[i][j] == False:
            dfs(i,j)
            result2 += 1


print(result, result2) # 정상, 색약
