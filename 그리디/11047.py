# 프로그램 소스코드 입력
# 동전0
import sys
n, k = map(int, sys.stdin.readline().split())
find = 0
count = 0
coin = []
for _ in range(n):
    A = int(sys.stdin.readline())
    coin.append(A)

coin.append(k)
coin.sort()
find = coin.index(k)

for j in range(find-1,-1,-1):
    count += k//coin[j]
    k %= coin[j]

print(count)