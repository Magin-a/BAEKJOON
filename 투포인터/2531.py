#회전 초밥
import sys
from collections import deque
input = sys.stdin.readline

#1.회전초밥 수, 2.초밥의 가짓수, 3.연속해서 먹는 접시 수, 4.쿠폰 번호
n, d, k, c= map(int, (input().split()))
data = [int(input().rstrip()) for _ in range(n)]
data.extend(data[:k])
result = 0
start = 0

while True:
    dish = []
    end = start + k

    if start > n-1:
        break

    for p in range(k):
        dish.append(data[start+p])


    if c not in dish: #쿠폰 초밥을 먹었는가 여부 확인
        dish.append(c)
        
    start += 1
    result = max(result, len(set(dish))) #최대 값 갱신

print(result) 
#pypy 통과 