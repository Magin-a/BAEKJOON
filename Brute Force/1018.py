#체스판 다시 칠하기
#브루트포스
import sys
input = sys.stdin.readline

n, m = map(int, input().split()) #행 열

g = []
result = []

for _ in range(n):
    g.append(list(input().strip()))

for a in range(n-7):
    for b in range(m-7):
        b_cnt = 0
        w_cnt = 0
        for x in range(a, a+8):
            for y in range(b, b+8):
                if (x+y)%2 == 0:
                    if g[x][y] != 'B':
                        b_cnt += 1
                    if g[x][y] != 'W':
                        w_cnt += 1

                else:      
                    if g[x][y] != 'W':
                        b_cnt += 1
                    if g[x][y] != 'B':
                        w_cnt += 1
        result.append(b_cnt)
        result.append(w_cnt)
print(min(result))
