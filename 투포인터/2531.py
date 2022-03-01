#회전 초밥
import sys
from collections import deque
input = sys.stdin.readline

#1.회전초밥 수, 2.초밥의 가짓수, 3.연속해서 먹는 접시 수, 4.쿠폰 번호
n, d, k, c= map(int, (input().split()))
data = deque([int(input().rstrip()) for _ in range(n)])
# start = 0
result = 0
for i in range(n):
    dish = []
    end = 0
    total = 0
    while True:
        if end >= k:
            break

        if data[end] in dish:
            break
        
        elif data[end] == c:
            dish.append(data[end])
            total += 1
            end += 1
            continue

        dish.append(data[end])
        total += 1
        end += 1
    
    # if c in dish:
    #     total += 1
    
    print(dish)
    result = max(result, total)
    data.rotate(-1)

print(result)
