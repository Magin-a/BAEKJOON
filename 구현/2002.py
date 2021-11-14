#추월 11/11~11.16
import sys
from collections import deque

car_cnt = int(sys.stdin.readline())
start = deque()
finish = deque()
result = 0
site = -1

for _ in range(car_cnt):
    start.append(sys.stdin.readline().strip())

for _ in range(car_cnt):
    finish.append(sys.stdin.readline().strip())

while start:
    site += 1
    a= start.popleft()
    
    if site <= finish.index(a):
        pass
    
    else:
        
        result += 1

print(result)


#2안
import sys
from collections import deque
car_cnt = int(sys.stdin.readline())
start = deque()
finish = deque()

for _ in range(car_cnt):
    start.append(sys.stdin.readline().strip())

for _ in range(car_cnt):
    finish.append(sys.stdin.readline().strip())

for a, b in enumerate(start):
    print(a, b)

cnt = 0
