#[인증평가(1차) 기출] 로봇이 지나간 경로
#사수가 조작한 로봇이 i행 j열을 방문했다면 #이고, 방문하지 않았다면 .이다.

import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split()) # column, row

find_x = [-1, 0, 1, 0]
find_y = [0, -1, 0, 1]
direction_str = ['<', '^', '>', 'v']

q = deque()

graph = [list(sys.stdin.readline().rstrip()) for _ in range(n)]

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
                f_y = y + find_y[a]

                if 0> f_x or f_x >= m or 0 >f_y or f_y >= n: 
                    cnt+=1
                    continue

                if graph[f_y][f_x] != '#':
                    cnt += 1

            if cnt == 3:
                return x, y
            

s_x, s_y = find()

print(s_y+1, s_x+1)
for i in range(4):
    y, x = s_y+find_y[i], s_x+find_x[i]
    if 0> x or x >= m or 0 > y or y >= n or  graph[y][x] != '#':         
            continue
    if graph[y][x] == '#':
        s_state = i
        print(direction_str[i])
        break
q.append([s_y, s_x])# 시작점 

# 이동 시작
while q:
    s_y, s_x = q.popleft()
    graph[s_y][s_x] = '.'

    for i in range(4):
        t_y = s_y + find_y[i]
        t_x = s_x + find_x[i]

        if 0> t_x or t_x >= m or 0 > t_y or t_y >= n or  graph[t_y][t_x] != '#':         
            continue

        elif  graph[t_y][t_x] == '#':
            #방향 잡기
            if direction_str[s_state] != direction_str[i]:
                left, right = s_state-1, s_state+1
                if right == 4:
                    right = 0

                if direction_str[left] == direction_str[i]:
                    print('L',end='')

                elif direction_str[right] == direction_str[i]:
                    print('R',end='')
            #방문처리
            graph[t_y][t_x] = '.'
            print('A', end='')
            graph[t_y + find_y[i]][t_x + find_x[i]]= '.'
            q.append([t_y + find_y[i], t_x + find_x[i]])
            s_state = i #현재 바라보는 방향 갱신