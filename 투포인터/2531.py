#회전 초밥
import sys
from collections import deque
input = sys.stdin.readline

#1.회전초밥 수, 2.초밥의 가짓수, 3.연속해서 먹는 접시 수, 4.쿠폰 번호
n, d, k, c= map(int, (input().split()))
data = deque([int(input().rstrip()) for _ in range(n)])

result = 0
for i in range(n):
    dish = []
    end = 0
    total = 0
    while True:
        if end >= k: #연속해서 먹은접시 목표량 달성 여부
            if c not in dish: #쿠폰 초밥을 먹었는가 여부 확인
                total += 1
            break

        if data[end] in dish:
            break

        dish.append(data[end])
        total += 1
        end += 1
    
    
    result = max(result, total) #최대 값 갱신
    data.rotate(-1) #초밥 회전

print(result) 