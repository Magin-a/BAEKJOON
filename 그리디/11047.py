#다시 풀이
# 동전0
import sys
from collections import deque
input = sys.stdin.readline

cnt, price = map(int, input().split())
result = 0
coin = []
for _ in range(cnt):
    coin.append(int(input()))

coin.sort(reverse= True)

coin = deque(coin)
while coin:
    current = coin.popleft()
    if current > price:
        continue

    result += (price//current)
    price %= current


print(result)
