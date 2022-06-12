#[인증평가(1차) 기출] 로봇이 지나간 경로
#사수가 조작한 로봇이 i행 j열을 방문했다면 #이고, 방문하지 않았다면 .이다.

import sys
input = sys.stdin.readline

n, m = map(int, input().split())

find_x = [-1, 0, 1, 0]
find_y = [0, -1, 0, 1]

graph = []
for _ in range(n):
    make = list(input().strip())
    graph.append(make)

#시작점 찾기
def find(x=0, y=0):
    
    for y in range(n):
        for x in range(m):
            if graph[y][x] != '#':
                continue
            cnt = 0
            now = graph[y][x]

            for a in range(4):
                f_x = x + find_x[a]
                f_y =  + find_y[a]

                if 0> f_x or f_x >= m or 0 >f_y or f_y >= n: 
                    cnt+=1
                    continue

                if graph[f_y][f_x] != '#':
                    cnt += 1

            if cnt == 3:
                return x, y
            

s_x, s_y = find()

print(s_x, s_y)
print(graph[s_y][s_x])

#시작 방향 잡기
for i in range(4):
    t_x = s_x + find_x[i]
    t_y = s_y + find_y[i]

    if graph[t_y][t_x] == '#':
        start_d = [find_x, find_y]
        if i == 0:
            print('<')

        elif i == 1:
            print('^')

        elif i == 2:
            print('>')

        elif i == 3:
            print('v')

        break



