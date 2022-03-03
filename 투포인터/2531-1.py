import sys
from collections import deque
input = sys.stdin.readline

#1.회전초밥 수, 2.초밥의 가짓수, 3.연속해서 먹는 접시 수, 4.쿠폰 번호
n, d, k, c= map(int, (input().split()))
data = [int(input().rstrip()) for _ in range(n)]
data.extend(data)
result = 0


for i in range(n):
    dish = data[i:i+4]
    total = 0
    dish.append(c)
    result = max(result, len(set(dish)))

print(result)

# a = [1, 2, 3, 4, 5, 6]

# test = a[0:4]
# print(test)