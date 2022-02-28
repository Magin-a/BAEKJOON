#동전
import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    coins = list(map(int, input().split()))
    goal = int(input())

    d = [0]*(goal+1)
    d[0] = 1

    for c in coins:
        for i in range(c, goal+1):
            d[i] += d[i-c]

    print(d[goal])