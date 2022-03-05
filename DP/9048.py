#동전
import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    coins = list(map(int, input().split()))
    goal = int(input())

    d = [0]*(goal+1) #goal(목표 금액)까지 DP 
    d[0] = 1

    for c in coins: #오름차순 코인
        for i in range(c, goal+1): 
            d[i] += d[i-c]  # 현재 i 는 (i- 현재 동전금액) => 이전 목표금액 달성 방법 수

    print(d[goal]) #목표 금액 달성방법 
