#이모티콘
import sys
from collections import deque
input = sys.stdin.readline

fin = int(input())
g = [[-1]*(fin+1) for _ in range(fin+1)]
q = deque()
q.append((1,0)) #화면 임티, 클립 임티
g[1][0] = 0

while q:
    s, c = q.popleft()
    
    if g[s][s] == -1:
        g[s][s] = g[s][c] + 1
        q.append((s,s))

    if s+c <=fin and g[s+c][s] == -1:
        g[s+c][c] = g[s][c] + 1
        q.append((s+c,c))

    if s-1 >= 0 and g[s-1][c] == -1:
        g[s-1][c] = g[s][c] + 1
        q.append((s-1,c))

ans = -1
for a in range(fin):
    if g[fin][a] != -1:
        if ans == -1 or ans > g[fin][a]:
            ans = g[fin][a]
print(ans)
print(g)   


#      0  1  2  3  4  5  6  7  8 
#dp = [0, 0, 2, 5, 4, 6, 5, 7, 6]
