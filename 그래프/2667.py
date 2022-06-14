#단지번호붙이기
import sys

input = sys.stdin.readline

n = int(input())
g = []
size = []

move_x = [-1, 0, 1, 0]
move_y = [0, -1, 0, 1]

for _ in range(n):
    g.append(list(map(int, input().strip())))

def dfs(y,x):
    global cnt #단지별 사이즈
    if x <= -1 or x >= n or y <= -1 or y >= n: #범위밖 조선
        return 0

    if g[y][x] == 1: #확인된 자리
        g[y][x] = 0
        cnt += 1

        for i in range(4):
            dfs(y+move_y[i], x+move_x[i])

        return cnt
    return 0


for a in range(n):
    for b in range(n):
        cnt = 0
        result = dfs(a, b)

        if result != 0:
            size.append(result)

print(len(size)) #단지 갯수
size = sorted(size)  #정렬
for i in size: 
    print(i)
    