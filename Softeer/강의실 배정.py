import sys
import heapq
input = sys.stdin.readline

n = int(input())

time = []
w = 0 
cnt = 0

for _ in range(n):
    start, fin = map(int, input().split())
    heapq.heappush(time, (fin, start))

print(time)
while time:
    f, s = heapq.heappop(time)

    if s >= w:
        cnt += 1
        w = f

print(cnt)

###########################################################
#소프티어 오답 코드
import sys
input = sys.stdin.readline
n = int(input())
bol = [list(map(int, input().split())) for _ in range(n)]

bol = sorted(bol, key=lambda x:(x[0], x[1]))

pre = [0, 0]
cnt = 0

for i in bol:
    if i[0] > pre[0] and i[1] < pre[1]:
        pre = i
        continue

    if pre[1] <= i[0]:
        pre = i
        cnt += 1

print(cnt)