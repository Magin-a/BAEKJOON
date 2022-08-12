#색종이 만들기
#분할 정복, 재귀
import sys
input = sys.stdin.readline

n = int(input())

g = [list(map(int, input().split())) for _ in range(n)]
result_w = 0
result_b = 0

def divide(x, y, n):
    global result_w, result_b
    now = g[x][y]
    for i in range(x, x+n):
        for j in range(y, y+n):
            if now != g[i][j]:
                divide(x,y, n//2)
                divide(x+n//2,y, n//2)
                divide(x,y+n//2, n//2)
                divide(x+n//2,y+n//2, n//2)
                return
    
    if now == 0:
        result_w += 1
        return
    elif now == 1:
        result_b += 1 
        return 




divide(0, 0, n)
print(result_w)
print(result_b)