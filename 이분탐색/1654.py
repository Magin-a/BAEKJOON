#랜선 자르기
#이분탐색, 매개변수 탐색 https://www.acmicpc.net/problem/1654
import sys
input = sys.stdin.readline

k, n = map(int, input().split())
bol = []
for _ in range(k):
    bol.append(int(input()))

mid = sum(bol)/len(bol)

while 1:
    cnt = 0
    for i in bol:
        cnt += i//mid
        