#봄버맨
#봄버맨
import sys
from collections import deque
r, c, n = map(int, sys.stdin.readline().split())

move = [[-1,0],[1, 0],[0, 1],[0, -1]]
boom = deque()
find_site = deque()
#폭탄위치 확인
for i in range(r):
    a = sys.stdin.readline().rstrip()
    for x,y in enumerate(a):
        if y == '.':
            continue
        else:
            boom.append([i,x])

#첫번째 폭탄 폭발
while boom:
    boom_site = boom.popleft()
    
