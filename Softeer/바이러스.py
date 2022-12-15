#바이러스
import sys
input = sys.stdin.readline

k, p, n = map(int, input().split())

result = (k*pow(p,n)+int(1e9+7))%int(1e9+7)
print(result)

