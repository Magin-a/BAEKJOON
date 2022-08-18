#징검다리2
import sys
input =sys.stdin.readline

n = int(input())

rock = list(map(int, input().split()))

up = [False] * n
down = [False] * n

for i in range(n-1):
    s, f = rock[i], rock[i+1]
    if s < f:
        up[i] = True

    if s > f:
        down[i] = True

if rock[n-2] > rock[n-1]:
        down[n-1] = True

print(up)
print(down)