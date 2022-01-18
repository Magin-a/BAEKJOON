#개미
import sys
from collections import deque
input = sys.stdin.readline

g1_cnt, g2_cnt = map(int, input().split())
g1 = deque(map(str, input().rstrip()))
g1.reverse()
g2 = deque(map(str, input().rstrip()))
time = int(input())


while time:
    if len(g2) == 0:
        break
    test = g2.popleft()
    g1.insert(len(g1)-time, test)
    time -= 1


result = g1 + g2
for ant in result:
    print(ant, end='')
