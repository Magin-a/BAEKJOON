#토너먼트
import sys
input = sys.stdin.readline

n, f_1, f_2 = map(int ,input().split())
cnt = 0
while f_1 != f_2:
    f_1 -= f_1//2
    f_2 -= f_2//2
    cnt += 1

print(cnt)
