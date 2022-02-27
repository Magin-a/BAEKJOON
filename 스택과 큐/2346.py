#풍선 터트리기
import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
q = deque(enumerate(map(int, input().split())))
result =[]

while q:
    idx, data = q.popleft()
    result.append(idx+1)

    if data < 0:
        q.rotate(-data)

    elif data > 0:
        q.rotate(data-1)

print(result)