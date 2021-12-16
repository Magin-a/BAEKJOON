#수 정렬하기 3
import sys
n = int(sys.stdin.readline())

result = [0]*10001

for _ in range(n):
    result[int(sys.stdin.readline())] += 1

for i in range(10001):
    if result[i] != 0:
        for a in range(result[i]):
            print(i)

#시간복잡도 주의!
