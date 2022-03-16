#유기농 배추
import sys
from collections import deque
input = sys.stdin.readline

move_row = [0, 1, 0, -1]
move_col = [-1, 0, 1, 0]


def bfs(row, col, graph):
    d = deque()
    d.append([row,col])
    graph[row][col] = 0

    while d:
        x,y = d.popleft()

        for i in range(4):
            test_row = x+move_row[i]
            test_col = y+move_col[i]

            if test_row < 0 or test_row >= n or test_col < 0 or test_col >= m:
                continue
        
            if graph[test_row][test_col] == 1:
                graph[test_row][test_col] = 0
                d.append([test_row, test_col])

    return


#입력부
t = int(input())

for _ in range(t):
    m, n, k = map(int, input().split()) 
    graph = [[0]*m for _ in range(n)]
    result = 0

    for _ in range(k): # 배추 위치 변환
        a, b = map(int, input().split())
        graph[b][a] = 1

    #탐색
    for x in range(n): 
        for y in range(m):
            if graph[x][y] == 1:
                bfs(x, y, graph)
                result += 1  

    print(result)