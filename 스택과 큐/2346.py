#풍선 터트리기
import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
q = deque(enumerate(map(int, input().split())))

while q:
    idx, data = q.popleft()
    print(idx+1, end=" ")

    if data < 0:# rotate(음수) => index = 0 값 뒤로 보내기 
        q.rotate(-data)

    elif data > 0:# rotate(양수) => index = -1 앞으로 당기기
        q.rotate(-(data-1))