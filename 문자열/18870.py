#좌표 압축
from audioop import reverse
import sys

input = sys.stdin.readline

n = int(input())
num_cnt = list(map(int , input().split()))

test = sorted(list(set(num_cnt)))
result = dict()

for index, a in enumerate(test):
    if a not in result:
        result[a] = index

for b in num_cnt:
    print(result.get(b),'', end='')
