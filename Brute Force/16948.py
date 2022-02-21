#데스 나이트
import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
q = deque()
graph = [[0]*n for _ in range(n)]
knight_x, knight_y, fin_x, fin_y = map(int, input().split()) #데스나이트 출발지점과 도착지점

move_x = [-2, 0, 2 ,2, 0, -2]
move_y = [-1, -2 ,-1, 1, 2, 1]

def bfs(x, y):
    q.append([x, y])

    while q:
        x, y = q.popleft()
        for a in range(6): #데스나이트의 예상이동 위치
            test_x = x + move_x[a]
            test_y = y + move_y[a]

            if 0 <= test_x < n and 0 <= test_y < n and graph[test_x][test_y] == 0: #1. test_x, test_y가 그래프범위 2. 방문한적이 없는 위치
                graph[test_x][test_y] = graph[x][y] + 1 #이동하기전 위치 값 +1
                q.append([test_x, test_y]) 

            else:
                continue

            if [fin_x, fin_y] in q: #해당 위치에 도착
                return graph[fin_x][fin_y]
    
    #모든 탐색 후 값이 없다면
    return -1

result = bfs(knight_x, knight_y)
print(result)
