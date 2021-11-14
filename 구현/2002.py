#추월 11/11~11.16
import sys
from collections import deque

car_cnt = int(sys.stdin.readline()) #차량 수

start = deque()
finish = deque()
cnt = 0

for x in range(car_cnt):
    start.append(sys.stdin.readline().strip())

for y in range(car_cnt):
    finish.append(sys.stdin.readline().strip())

while start: #터널 입장 차량 순서 
    car = start.popleft() # 터널 입장순서대로 pop
    
    if car in finish: # car가 finish에 있다면 조건1 충족
        while car != finish[0]: #입장 순서와 다르다면 추월한 차량으로 간주
            finish.popleft() #해당 car가 나올때까지 pop
            cnt += 1 #조건 충족시 추월 차량으로 간주
            
        else:
            finish.popleft() #finish에서 해당 car를 찾으면 pop, 하지만 cnt는 하지 않음 
    else:
        pass #해당 car는 이전에 추월한 차량

print(cnt) #최종 추월한 차량
